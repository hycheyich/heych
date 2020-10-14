import  random
from datetime import datetime
from rest_framework import serializers
from django.db import transaction
from django_redis import get_redis_connection
from courses.models import Course, CourseExpire
from .models import OrderDetail, Order


class OrderModelSerializer(serializers.Serializer):
    """
    订单序列化器
    """

    class Meta:
        model = Order
        fields = ["order_number", "pay_type", "credit", "coupon"]
        read_only_fields = ["order_number"]
        extra_kwargs = {
            "pay_type": {"write_only": True, "required": True},
            "credit": {"write_only": True},
            "coupon": {"write_only": True},
        }

    def validate(self, attrs):
        # todo 校验是否使用了积分
        # todo 校验是否使用了优惠券，优惠券在有效使用期间
        return attrs

    def create(self, validated_data):
        """
        生成订单
        @param validated_data:  表示校验过的数据
        @return:
        """
        # 接收客户端提交的数据
        # 支付方式
        # pay_type = validated_data.get('pay_type')
        # # 使用积分数量
        # credit = validated_data.get('credit', 0)
        # # 用户优惠券ID
        # coupon = validated_data.get('coupon', 0)
        user_id = self.context["request"].user.id  # 在序列化器中获取视图中的数据
        # order_title = "路飞学城课程购买"
        order_number = datetime.now().strftime("%Y%m%d%H%M%S") + ("%06d" % user_id) + ("%04d" % random.randint(0, 9999))
        # 开始编写保存订单信息和订单详情模型的代码
        with transaction.atomic():  # 开启事务的自动提交
            # 设置回滚点
            save_id = transaction.savepoint()
            # 1 生成订单
            try:
                order = Order.objects.create(
                    order_title="路飞学城课程购买",
                    total_price=0,
                    real_price=0,
                    order_number=order_number,
                    pay_type=validated_data.get("pay_type"),
                    credit=validated_data.get("credit"),
                    coupon=validated_data.get("coupon"),
                    user_id=user_id,
                )
                # 2 连接redis
                redis_conn = get_redis_connection('cart')

                # 3 到redis 中提取对应用户的购物车
                cart_hash = redis_conn.hgetall(f'cart_{user_id}')
                selected_id_set = redis_conn.smembers(f"selected_{user_id}")
                # 判断勾选项是否为空，为空表示没有订单
                if selected_id_set is None:
                    transaction.savepoint_rollback(save_id)
                    return serializers.ValidationError('对不起，购物车没有勾选的商品')

                # 4 提取 购物车中勾选的商品信息
                total_price = 0
                pipe = redis_conn.pipeline()  # 开始redis 事务
                pipe.multi()
                for course_id_bytes in selected_id_set:
                    course_id = course_id_bytes.decode()
                    expire = int(cart_hash[course_id_bytes].decode())
                    try:
                        course = Course.objects.get(pk=course_id, is_show=True, is_delete=False)
                    except Course.DoesNotExist:
                        # 表示商品已经下架了
                        continue
                    # 提取出课程有效期
                    try:
                        ret = CourseExpire.objects.get(course_id=course_id, expire=expire)
                        expire = ret.expire
                    except:
                        expire = 0
                    # 5  把循环中每一个商品添加到订单详情里面
                    real_price = course.get_discount_price_by_expire(expire)
                    OrderDetail.objects.create(
                        order=order,
                        course=course,
                        expire=expire,
                        price=course.get_price_by_expire(expire),
                        real_price=real_price,
                        discount_name=course.discount_name
                    )
                    # 6. 从redis中删除对应已经添加到订单里面的商品
                    pipe.hdel("cart_%s" % user_id, course_id)
                    pipe.srem("selected_%s" % user_id, course_id)
                    # 计算商品总价
                    total_price += float(real_price)
                    pipe.execute()

                    # 更新订单的总价
                    order.total_price = total_price  # 订单总价，不涉及积分和优惠券的抵扣
                    order.real_price = total_price  # 订单实付价，在订单总价的基础上，扣除了积分和优惠券
                    order.save()

            except:
                transaction.savepoint_rollback(save_id)
                raise serializers.ValidationError("生成订单失败！")
        # 6. 返回订单的生成结果
        return order





