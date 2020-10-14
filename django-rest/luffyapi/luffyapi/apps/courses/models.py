from datetime import datetime
from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from luffyapi.utils.models import BaseModel

# Create your models here.
class CourseCategory(BaseModel):
    """
    课程分类
    """
    name = models.CharField(max_length=64, unique=True, verbose_name="分类名称")

    class Meta:
        db_table = "ly_course_category"
        verbose_name = "课程分类"
        verbose_name_plural = "课程分类"

    def __str__(self):
        return "%s" % self.name


class Course(BaseModel):
    """
    实战课程
    """
    course_type = (
        (0, '付费'),
        (1, 'VIP专享'),
        (2, '学位课程'),
    )
    level_choices = (
        (0, '初级'),
        (1, '中级'),
        (2, '高级'),
    )
    status_choices = (
        (0, '上线'),
        (1, '下线'),
        (2, '预上线'),
    )
    name = models.CharField(max_length=128, verbose_name="课程名称")
    course_img = models.ImageField(upload_to="course", max_length=255, verbose_name="封面图片", blank=True, null=True)
    course_video = models.FileField(upload_to="course_video", max_length=255, verbose_name="封面视频", blank=True,
                                    null=True)
    course_type = models.SmallIntegerField(choices=course_type, default=0, verbose_name="付费类型")
    # 使用这个字段的原因
    brief = models.TextField(verbose_name="详情介绍", null=True, blank=True)
    level = models.SmallIntegerField(choices=level_choices, default=1, verbose_name="难度等级")
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)
    period = models.IntegerField(verbose_name="建议学习周期(day)", default=7)
    attachment_path = models.FileField(max_length=128, verbose_name="课件路径", blank=True, null=True)
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="课程状态")
    course_category = models.ForeignKey("CourseCategory", on_delete=models.CASCADE, null=True, blank=True,
                                        verbose_name="课程分类")
    students = models.IntegerField(verbose_name="学习人数", default=0)
    lessons = models.IntegerField(verbose_name="总课时数量", default=0)
    pub_lessons = models.IntegerField(verbose_name="课时更新数量", default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="课程原价", default=0)
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="授课老师")

    class Meta:
        db_table = "ly_course"
        verbose_name = "实战课程"
        verbose_name_plural = "实战课程"

    def __str__(self):
        return "%s" % self.name

    @property
    def level_name(self):
        return self.get_level_display()

    @property
    def free_lesson_list(self):
        """
        推介课时列表
        """
        data = []
        lesson_list = self.lesson_list.filter(is_show=True, is_delete=False, recomment=True)
        for lesson in lesson_list:
            data.append({
                "id": lesson.id,
                'name': lesson.name,
                'free_trail': lesson.free_trail,
                'lesson': lesson.lesson
            })

        return data

    @property
    def expire_list(self):
        """
        当前课程的有效期列表
        @return:
        """
        data_list = []
        # 查找出课程有效期表中上线的数据
        result = self.courseexpire.filter(is_show=True, is_delete=False).order_by("orders")
        # 因课程表中也有价钱，此价钱表示课程永久有效的价钱，课程有效期中的价钱表示相应的课程对应相应的价钱，所以这里需要做判断
        # 获取queryset列表中每个对象
        for item in result:
            data_list.append({
                'exprie': item.expire,  # 课程有效期天数
                'text': item.text,  # 课程有效期提示
                'price': item.price,  # 价钱
            })
        if self.price > 0:
            data_list.append({
                'expire': 0,  # 0 表示永久有效
                'text': '永久有效',
                'price': self.price,
            })
        return data_list

    def get_price_by_expire(self, expire):
        """
        获取有效期对应的价格
        @param expire:
        @return:
        """
        if int(expire) > 0:
            """从课程有效期选项列表中提取价格"""
            obj = self.courseexpire.get(expire=expire)
            return obj.price
        else:
            """从课程模型中提取价格"""
            return self.price

    @property
    def get_course_activity(self):
        """
        获取当前课程参加的活动
        分析：
            1、判断过期时间，是否存在已经过期的
        @return:
        """
        now_time = datetime.now()
        # 活动开始时间小于当前时间，活动结束时间大于当前时间
        return self.course_prices.get(activity__start_time__lte=now_time, activity__end_time__gte=now_time)

    @property
    def discount_name(self):
        """
        当前课程参与活动的优惠类型
        @return:
        """
        try:
            ret = self.get_course_activity
            return ret.discount.discount_type.name
        except:
            # 没有参与到活动中
            return ""

    # @property
    def discount_price(self, price=None):
        """
        当前课程参与活动的优惠实价
        分析：
            1、 查询 CourseActivity  课程   策略  活动 三者之间的关系
                获取当前课程参与的活动，返回的是活动对象
            2、
        @return:
        """
        if price is None:
            price = self.price

        price = float(self.price)
        try:
            # 获取当前课程参与的活动
            ret = self.get_course_activity
            # 满足优惠的价格条件 如果大于原价的话,表示没有达到参与活动的价格条件
            if ret.discount.condition > price:
                return -1
            # 获取当前课程的参与的活动对应的优惠公式
            sale = ret.discount.sale
            # 此处根据 课程优惠策略模型 中的规则进行判断
            if sale == "0":
                # 表示限时免费
                return 0
            if sale[0] == "*":
                # 限时折扣
                discount = float(sale[1:])
                return price * discount
            if sale[0] == "-":
                # 限时减免
                discount = float(sale[1:])
                return price - discount

            if sale[0] == '满':
                dis_list = sale.split("\n")
                dis_arr = []  # 当前课程能满足的所有所有满减优惠值
                for dis_item in dis_list:
                    discount_condition, discount_price = dis_item[1:].split("-")
                    if float(discount_condition) < price:
                        dis_arr.append(float(discount_price))

                    discount = max(dis_arr)
                    return price - discount
            # 没有或者未知的活动
            return -1
        except:
            # 没有参与到活动中
            return -1

    @property
    def has_time(self):
        """课程参与活动以后的倒计时"""
        try:
            ret = self.get_course_activity
            end_time_stamp = ret.activity.end_time.timestamp()  # 活动结束时的数值时间戳
            now_time_stamp = datetime.now().timestamp()  # 当前时间的数值时间戳
            return int(end_time_stamp - now_time_stamp)
        except:
            return -1

    def get_discount_price_by_expire(self, expire):
        """根据课程购买有效期选项获取真实的优惠价格"""
        price = self.get_price_by_expire(expire)  # 根据有效期选项获取课程对应的原价
        discount_price = self.discount_price(price)  # 根据原价获取当前课程的优惠价格
        if discount_price == -1:
            return price
        else:
            return discount_price


class Teacher(BaseModel):
    """讲师、导师表"""
    role_choices = (
        (0, '讲师'),
        (1, '导师'),
        (2, '班主任'),
    )
    name = models.CharField(max_length=32, verbose_name="讲师昵称")
    role = models.SmallIntegerField(choices=role_choices, default=0, verbose_name="讲师身份")
    title = models.CharField(max_length=64, verbose_name="职位、职称")
    signature = models.CharField(max_length=255, verbose_name="导师签名", help_text="导师签名", blank=True, null=True)
    image = models.ImageField(upload_to="teacher", null=True, blank=True, verbose_name="讲师封面")
    brief = models.TextField(max_length=1024, verbose_name="讲师描述")

    class Meta:
        db_table = "ly_teacher"
        verbose_name = "讲师导师"
        verbose_name_plural = "讲师导师"

    def __str__(self):
        return "%s" % self.name


class CourseChapter(BaseModel):
    """课程章节"""
    course = models.ForeignKey("Course", related_name='chapters', on_delete=models.CASCADE, verbose_name="课程名称")
    chapter = models.SmallIntegerField(verbose_name="第几章", default=1)
    name = models.CharField(max_length=128, verbose_name="章节标题")
    summary = models.TextField(verbose_name="章节介绍", blank=True, null=True)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)

    class Meta:
        db_table = "ly_course_chapter"
        verbose_name = "课程章节"
        verbose_name_plural = "课程章节"

    def __str__(self):
        return "%s:(第%s章)%s" % (self.course, self.chapter, self.name)


class CourseLesson(BaseModel):
    """课程课时"""
    lesson_type_choices = (
        (0, '文档'),
        (1, '练习'),
        (2, '视频')
    )
    chapter = models.ForeignKey("CourseChapter", related_name='lessons', on_delete=models.CASCADE, verbose_name="章节")
    course = models.ForeignKey("Course", related_name="lesson_list", on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=128, verbose_name="课时标题")
    lesson_type = models.SmallIntegerField(default=2, choices=lesson_type_choices, verbose_name="课时种类")
    lesson_link = models.CharField(max_length=255, blank=True, null=True, verbose_name="课时链接",
                                   help_text="若是video，填vid,若是文档，填link")
    duration = models.CharField(verbose_name="视频时长", blank=True, null=True, max_length=32)  # 仅在前端展示使用
    pub_date = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)
    free_trail = models.BooleanField(verbose_name="是否可试看", default=False)
    recomment = models.BooleanField(verbose_name="是否推荐到课程列表")
    lesson = models.IntegerField(default=1, verbose_name="课时序号，第几节")

    class Meta:
        db_table = "ly_course_lesson"
        verbose_name = "课程课时"
        verbose_name_plural = "课程课时"

    def __str__(self):
        return "%s-%s" % (self.chapter, self.name)


class CourseExpire(BaseModel):
    """
    课程有效期
    """
    course = models.ForeignKey("Course", related_name='courseexpire', on_delete=models.CASCADE, verbose_name="课程ID")
    expire = models.CharField(max_length=100, verbose_name="课程有效期(天)", help_text="课程有效期")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="课程价格", default=0)
    text = models.CharField(max_length=100, verbose_name="文本提示", help_text="文本提示", default='3天有效')

    class Meta:
        db_table = "ly_course_expire"
        verbose_name = "课程与有效期"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % (self.course)


"""价格相关的模型"""


class PriceDiscountType(BaseModel):
    """课程优惠类型"""
    name = models.CharField(max_length=32, verbose_name="类型名称")
    remark = models.CharField(max_length=250, blank=True, null=True, verbose_name="备注信息")

    class Meta:
        db_table = "ly_price_discount_type"
        verbose_name = "课程优惠类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % (self.name)


class PriceDiscount(BaseModel):
    """课程优惠策略模型"""
    discount_type = models.ForeignKey("PriceDiscountType", on_delete=models.CASCADE, related_name='pricediscounts',
                                      verbose_name="优惠类型")
    condition = models.IntegerField(blank=True, default=0, verbose_name="满足优惠的价格条件")
    sale = models.TextField(verbose_name="优惠公式", help_text="""
    0表示免费；<br>
    *号开头加上浮点数表示折扣价，例如*0.82表示八二折；<br>
    -号开头加上整数表示减免价格，例如-50表示减免50元；<br>
    如果要表示限时满减,则需要使用 原价-优惠价格,例如表示,课程价格大于100,优惠10;大于200,优惠20,格式如下:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;满100-10<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;满200-20<br>
    """)

    class Meta:
        db_table = "ly_price_discount"
        verbose_name = "价格优惠策略"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "价格优惠:%s,优惠条件:%s,优惠值:%s" % (self.discount_type.name, self.condition, self.sale)


class Activity(BaseModel):
    """优惠活动模型"""
    name = models.CharField(max_length=64, verbose_name="活动名称")
    start_time = models.DateTimeField(verbose_name="活动的开始时间", help_text="活动的开始时间")
    end_time = models.DateTimeField(verbose_name="活动的结束时间", help_text="活动的结束时间")

    class Meta:
        db_table = "ly_activity"
        verbose_name = "优惠活动表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s[%s-%s]" % (self.name, self.start_time, self.end_time)


class CourseActivity(BaseModel):
    """课程与活动的关系模型"""
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="course_prices", verbose_name="课程")
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE, related_name="activity_courses",
                                 verbose_name='优惠活动')
    discount = models.ForeignKey("PriceDiscount", on_delete=models.CASCADE, related_name="discount_courses",
                                 verbose_name="优惠策略")

    class Meta:
        db_table = "ly_course_activity"
        verbose_name = "课程与优惠活动的关系"
        verbose_name_plural = "课程与优惠策略的关系"

    def __str__(self):
        return "%s-%s-%s" % (self.course.name, self.activity.name, self.discount.discount_type.name)
