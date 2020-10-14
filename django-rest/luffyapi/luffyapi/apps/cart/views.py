from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django_redis import get_redis_connection
from rest_framework.permissions import IsAuthenticated
from courses.models import Course, CourseExpire

# Create your views here.
# 添加商品到购物车
# 前端发送课程id ，用户id，
# 分析 ：
#     存入redis数据库中数据的种类以及方式
#      用户id  课程id  有效期    hash
#       用户id   课程勾选状态   集合

import logging

log = logging.getLogger('购物车')


class CartAPIView(ViewSet):
    permission_classes = [IsAuthenticated]

    def add_cart(self, request):
        """
        添加商品到购物车
        @param request:
        @return:
        """
        # 获取用户id
        user_id = request.user.id
        # 获取前端发送的课程id
        course_id = request.data.get('course_id')
        # 查询mysql数据库是否存在此数据，或者是上架的数据
        try:
            course_obj = Course.objects.get(pk=course_id, is_show=True, is_delete=False)
        except:
            return Response({'message': '对不起找不到您的商品'}, status=status.HTTP_404_NOT_FOUND)

        # todo 判断用户是否已经购买了本商品，如果购买了本商品并且在有效期内，就不添加购物车了

        # 连接redis数据库
        redis_conn = get_redis_connection('cart')
        # 插入数据
        # 设置有效期和勾选状态的默认值
        expire = 0
        # 0表示没有设置默认值，或者将来我们完成课程的有效期时，重新定义0代表的意思

        pipe = redis_conn.pipeline()
        pipe.multi()  # 开启事务
        pipe.hset(f'cart_{user_id}', course_id, expire)
        pipe.sadd(f'selected_{user_id}', course_id)
        # 默认勾选的状态，如果用户不希望将来这个商品进行结算状态，我们在购物车商品列表中提供按钮给用户去掉
        pipe.execute()
        # 获取商品总数
        cart_length = redis_conn.hlen("cart_%s" % user_id)
        # 返回响应结果
        return Response({'message': '成功添加商品到购物车', 'cart_length': cart_length})

    def get_cart_list(self, request):
        """
        获取加入购物车中的商品信息
        @param request:
        @return:
        """
        user_id = request.user.id
        # 连接redis数据库
        redis_conn = get_redis_connection('cart')
        # 获取课程
        cart_dict_bytes = redis_conn.hgetall(f'cart_{user_id}')
        # 获取勾选状态
        selectd_set_bytes = redis_conn.smembers(f'selected_{user_id}')
        data = []
        # 循环字典，获取课程id 已经有效期
        for course_id_bytes, expire_bytes in cart_dict_bytes.items():
            course_id = course_id_bytes.decode()
            expire = expire_bytes.decode()
            try:
                course = Course.objects.get(pk=course_id, is_show=True, is_delete=False)
            except Course.DoesNotExist:
                continue
            if course:
                data.append({
                    'course_id': course.id,
                    'course_name': course.name,
                    'course_img': course.course_img.url,
                    # 'price': course.get_price_by_expire(expire),  # 课程原价
                    'expire': expire,  # 有效期时间  数字
                    'selected': course_id_bytes in selectd_set_bytes,  # 判断课程是否勾选
                    'expire_list': course.expire_list,  # 课程有效期列表
                    # todo 后面实现课程购买有效期以后返回有效期选项列表
                    "price": course.get_discount_price_by_expire(expire),
                })
        return Response(data, status=status.HTTP_200_OK)

    def change_selected_status(self, request):
        """
        改变勾选状态
        分析：
            改变勾选状态 前端需要发送字段
            用户id   课程id   勾选状态
        @param request:
        @return:
        """
        # 获取用户id
        user_id = request.user.id
        # 获取课程id
        course_id = request.data.get('course_id')

        # 获取勾选状态
        course_list = []
        selected = request.data.get('selected')
        if type(course_id) == list:
            # 表示全选
            for i in course_id:
                course_list.append(i.get('course_id'))
            course_id = course_list

        # 连接redis
        redis_conn = get_redis_connection('cart')
        # 切换状态
        if selected:
            # 勾选
            if isinstance(course_id, list):
                redis_conn.sadd("selected_%s" % user_id, *course_id)
            else:
                redis_conn.sadd("selected_%s" % user_id, course_id)
        else:
            # 未勾选
            if isinstance(course_id, list):
                print(isinstance(course_id, list))
                redis_conn.srem("selected_%s" % user_id, *course_id)
            else:
                redis_conn.srem("selected_%s" % user_id, course_id)

        return Response({'message': '切换状态成功'})

    def delete_course(self, request):
        """
        删除购物车中的商品
        分析：
            获取前端 用户id  商品id
        drf中,接受put,patch和post,接收请求体都使用request.data
        接受get,delete,接收参数，只能使用request.query_params,
        原因是: http请求中.get,delete是没有请求体的.而post,put和patch有请求体
        axios.request（config）
        axios.get（url [，config]）
        axios.delete（url [，config]）
        axios.head（url [，config]）
        axios.options（url [，config]）
        axios.post（url [，data [，config]]
        axios.put（url [，data [，config]]）
        axios.patch（url [，data [，config]]）
        @param request:
        @return:
        """
        # 获取用户id
        user_id = request.user.id
        # from rest_framework import request
        # 获取商品id
        course_id = request.query_params.get('course_id')
        try:
            Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"message": "删除商品数据成功"})
        # 连接数据库
        redis_conn = get_redis_connection('cart')
        # # 采用事务方式
        pipe = redis_conn.pipeline()
        pipe.multi()
        # 删除数据
        pipe.hdel(f"cart_{user_id}", course_id)
        pipe.srem(f"selected_{user_id}", course_id)
        pipe.execute()

        return Response({'message': '删除数据成功'})

    # def change_course_expire(self, request):
    #     """
    #     通过改变课程有效期改变价钱
    #     分析：
    #         1、获取user_id
    #         2、课程id
    #         3、有效期id
    #         4、返回有效期对应的价钱，0表示永久有效，返回原价，非0表示不是永久有效，返回课程有效期表中的价钱
    #     @param request:
    #     @return:
    #     """
    #     user_id = request.user.id
    #     course_id = request.data.get("course_id")
    #     expire_id = request.data.get("expire_id")
    #     try:
    #         Course.objects.get(pk=course_id, is_show=True, is_delete=False)
    #     except Course.DoesNotExist:
    #         # 表示不存在
    #         return Response({"message": "对不起，当前商品已下架或不存在！"}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # 判断有效期
    #     if expire_id > 0:
    #         # 表示不是永久有效
    #         try:
    #             CourseExpire.objects.get(course_id=course_id, pk=expire_id, is_show=True, is_delete=False, )
    #         except CourseExpire.DoesNotExist:
    #             # 表示课程有效期不存在
    #             return Response({"message": "对不起，当前商品的有效期选项不存在！"}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # 连接redis
    #     try:
    #         redis = get_redis_connection("cart")
    #         redis.hset("cart_%s" % user_id, course_id, expire_id)
    #     except:
    #         log.error("redis数据库操作出错！")
    #         return Response({"message": "对不起，切换商品有效期选项有误！请联系客服工作人员！"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    #
    #         # 返回结果[对应有效期的价格]
    #     return Response({"message": "切换商品有效期选项成功！", "price": expire.price}, status=status.HTTP_200_OK)

    def change_expire(self, request):
        """
        切换课程有效期选项
        @param request:
        @return:
        """
        user_id = request.user.id
        course_id = request.data.get("course_id")
        expire_id = request.data.get("expire_id")
        print(request.data)
        try:
            Course.objects.get(pk=course_id, is_show=True, is_delete=False)
        except Course.DoesNotExist:
            # 表示不存在
            return Response({"message": "对不起，当前商品已下架或不存在！"}, status=status.HTTP_400_BAD_REQUEST)
        # todo 切换有效期bug未修复，前端course.expire的问题
        print(expire_id)
        # 判断有效期
        if expire_id > 0:
            # 表示不是永久有效
            try:
                CourseExpire.objects.get(course_id=course_id, pk=expire_id, is_show=True, is_delete=False, )
            except CourseExpire.DoesNotExist:
                # 表示课程有效期不存在
                return Response({"message": "对不起，当前商品的有效期选项不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        # 连接redis
        redis = get_redis_connection("cart")
        # 修改课程有效期
        redis.hset("cart_%s" % user_id, course_id, expire_id)
        return Response({"message": "修改有效期选项成功！"})

    def get_select_course(self, request):
        """
        获取勾选的课程，因为订单表示的都是勾选的课程
        获取用户id
        @param request:
        @return:
        """
        user_id = request.user.id
        # 根据用户id查找勾选的课程

        # 连接redis数库
        redis_conn = get_redis_connection('cart')
        cart_hash = redis_conn.hgetall(f'cart_{user_id}')
        select_set = redis_conn.smembers(f'selected_{user_id}')
        # 根据购物车中的商品id到mysql中提取商品具体信息
        data = []

        for course_id_bytes in select_set:
            course_id = course_id_bytes.decode()
            expire = int(cart_hash[course_id_bytes].decode())  # 查找有效期

            try:
                course = Course.objects.get(pk=course_id, is_show=True, is_delete=False)
            except Course.DoesNotExist:
                # 如果课程下架了，继续查找

                continue

            try:
                ret = CourseExpire.objects.get(course_id=course_id, expire=expire)
                expire_text = ret.text
            except:
                expire_text = "永久有效"

            data.append({
                "course_id": course.id,
                "course_img": course.course_img.url,
                "course_name": course.name,
                "discount_name": course.discount_name,
                "expire_text": expire_text,
                "original_price": course.get_price_by_expire(expire),
                "discount_price": course.get_discount_price_by_expire(expire),
            })
            # 返回结果
        return Response(data)

# todo 前端视频播放未实现
# todo 前端富文本框未实现
