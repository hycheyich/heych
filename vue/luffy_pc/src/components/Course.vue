<template>
  <div class="course">
    <Header></Header>
    <div class="main">
      <!-- 筛选条件 -->
      <div class="condition">
        <ul class="cate-list">
          <li class="title">课程分类:</li>
          <li :class="category==0?'this':''" @click="category=0">全部</li>
          <li
            :class="category==item.id?'this':''"
            :key="key"
            v-for="(item,key) in category_list"
            @click="category=item.id"
          >{{item.name}}
          </li>
        </ul>

        <div class="ordering">
          <ul>
            <li class="title">筛&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;选:</li>
            <li class="default" :class="change_orders_class('id')" @click="change_orders('id')">默认</li>
            <li class="hot" :class="change_orders_class('students')" @click="change_orders('students')">人气</li>
            <li class="price" :class="change_orders_class('price')" @click="change_orders('price')">价格</li>
          </ul>
          <p class="condition-result">共21个课程</p>
        </div>
      </div>
      <!-- 课程列表 -->
      <div class="course-list">
        <div class="course-item" :key="index" v-for="(course,index) in course_list">
          <div class="course-image">
            <img :src="course.course_img" alt/>
          </div>
          <div class="course-info">
            <h3>
              <router-link :to="`/courses/${course.id}`">{{course.name}}</router-link>
              <span>
                <img src="/static/image/avatar1.svg" alt/>
                {{course.students}}人已加入学习
              </span>
            </h3>
            <p class="teather-info">
              {{course.teacher.name}} {{course.teacher.title}} {{course.teacher.signature}}
              <span>共{{course.lessons}}课时/{{course.pub_lessons==course.lessons?'更新完成':`已更新${course.pub_lessons}`}}</span>
            </p>
            <ul class="lesson-list">
              <li :key="key"
                  v-for="(free_lesson ,key) in course.free_lesson_list">
                <span class="lesson-title">0{{key+1}} | 第{{free_lesson.lesson}}节:{{free_lesson.name}}</span>
                <span class="free" v-if="free_lesson.free_trail">免费</span>
              </li>
            </ul>
            <div class="pay-box">
              <span class="discount-type" v-if="course.discount_name">{{course.discount_name}}</span>
              <span class="discount-price" v-if="course.discount_name">￥{{parseFloat(course.discount_price).toFixed(2)}}元</span>
               <span class="original-price" v-if="course.discount_name">原价：{{parseFloat(course.price).toFixed(2)}}元</span>
              <span class="discount-price" v-else>￥{{parseFloat(course.price).toFixed(2)}}元</span>
              <router-link :to="`/courses/${course.id}`"><span class="buy-now">立即购买</span></router-link>
            </div>
          </div>
        </div>
      </div>
      <div class="pagein">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="filters.page"
          :page-sizes="pageSizes"
          :page-size="filters.size"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
        </el-pagination>
      </div>
    </div>

    <Footer></Footer>
  </div>
</template>

<script>
  import Header from "./common/Header";
  import Footer from "./common/Footer";

  export default {
    name: "Course",
    data() {
      return {
        category: 0,
        category_list: [],  // 课程大类列表
        course_list: [],  // 课程列表
        pageSizes: [2, 5, 10, 20],
        total: 0,  // 当前课程列表中的课程总数
        filters: {
          // id表示默认正序，-id表示默认倒序，
          // students表示人气正序, -students表示人气倒序
          // price 表示价格正序, -price表示价格倒序
          ordering: "id",
          page: 1,
          size: 5,
        }
      };
    },
    created() {
      this.get_CourseCategory();
      this.get_course();
    },
    watch: {
      category() {
        //监听课程大类id
        this.get_course();
      },
      "filters.ordering": function () {
        // 切换排序方式
        // console.log(this.filters.ordering);
        this.get_course();
      },
      'filters.page': function () {
        this.get_course()
      }
    },
    methods: {
      get_CourseCategory() {
        //获取课程大类
        this.$axios
          .get(`${this.$settings.Host}/courses/coursecategory/`)
          .then(response => {
            this.category_list = response.data;
          })
          .catch(error => {
            this.$message.error("获取课程分类失败");
          });
      },
      get_course() {
        //获取课程
        //分类筛选条件
        if (this.category > 0) {
          this.filters.course_category = this.category;
        } else {
          delete this.filters.course_category;
        }
        this.$axios
          .get(`${this.$settings.Host}/courses/course`, {
            params: this.filters
          })
          .then(response => {
            this.course_list = response.data.results;
            this.total = response.data.count
          })
          .catch(error => {
            this.$message.error("获取课程失败");
          });
      },
      change_orders(type) {
        //改变排序
        // 切换排序方式
        if (this.filters.ordering === '-' + type) {
          this.filters.ordering = type;
        } else if (this.filters.ordering === type) {
          this.filters.ordering = '-' + type
        } else {
          this.filters.ordering = type;
        }
      },
      change_orders_class(type) {
        //改变排序的类
        let _class = "";
        if (type === this.filters.ordering) {
          _class = 'this asc'
        }
        if ('-' + type === this.filters.ordering) {
          _class = 'this desc'
        }
        return _class
      },
      handleSizeChange(size) {
        //单页数据量发生改变时触发事件
        this.filters.size = size;
        this.filters.page = 1;
        console.log(`每页 ${size} 条`);
      },
      handleCurrentChange(page) {
        //当前页码发生改变时触发的事件
        // console.log(`当前页: ${page}`);
        this.filters.page = page;

      }

    },
    components: {
      Header,
      Footer
    }
  };
</script>

<style scoped>
  .course {
    background: #f6f6f6;
  }

  .course .main {
    width: 1100px;
    margin: 35px auto 0;
  }

  .course .condition {
    margin-bottom: 35px;
    padding: 25px 30px 25px 20px;
    background: #fff;
    border-radius: 4px;
    box-shadow: 0 2px 4px 0 #f0f0f0;
  }

  .course .cate-list {
    border-bottom: 1px solid #333;
    border-bottom-color: rgba(51, 51, 51, 0.05);
    padding-bottom: 18px;
    margin-bottom: 17px;
  }

  .course .cate-list::after {
    content: "";
    display: block;
    clear: both;
  }

  .course .cate-list li {
    float: left;
    font-size: 16px;
    padding: 6px 15px;
    line-height: 16px;
    margin-left: 14px;
    position: relative;
    transition: all 0.3s ease;
    cursor: pointer;
    color: #4a4a4a;
    border: 1px solid transparent; /* transparent 透明 */
  }

  .course .cate-list .title {
    color: #888;
    margin-left: 0;
    letter-spacing: 0.36px;
    padding: 0;
    line-height: 28px;
  }

  .course .cate-list .this {
    color: #ffc210;
    border: 1px solid #ffc210 !important;
    border-radius: 30px;
  }

  .course .ordering::after {
    content: "";
    display: block;
    clear: both;
  }

  .course .ordering ul {
    float: left;
  }

  .course .ordering ul::after {
    content: "";
    display: block;
    clear: both;
  }

  .course .ordering .condition-result {
    float: right;
    font-size: 14px;
    color: #9b9b9b;
    line-height: 28px;
  }

  .course .ordering ul li {
    float: left;
    padding: 6px 15px;
    line-height: 16px;
    margin-left: 14px;
    position: relative;
    transition: all 0.3s ease;
    cursor: pointer;
    color: #4a4a4a;
  }

  .course .ordering .title {
    font-size: 16px;
    color: #888;
    letter-spacing: 0.36px;
    margin-left: 0;
    padding: 0;
    line-height: 28px;
  }

  .course .ordering .this {
    color: #ffc210;
  }

  .course .ordering .this {
    position: relative;
  }

  .course .ordering .this::before,
  .course .ordering .this::after {
    cursor: pointer;
    content: "";
    display: block;
    width: 0px;
    height: 0px;
    border: 5px solid transparent;
    position: absolute;
    right: 0;
  }

  .course .ordering .this::before {
    border-bottom: 5px solid #aaa;
    margin-bottom: 2px;
    top: 2px;
  }

  .course .ordering .this::after {
    border-top: 5px solid #aaa;
    bottom: 2px;
  }

  .course .ordering .asc::before {
    border-bottom: 5px solid #ffc210;
  }

  .course .ordering .desc::after {
    border-top: 5px solid #ffc210;
  }


  .course .course-item:hover {
    box-shadow: 4px 6px 16px rgba(0, 0, 0, 0.5);
  }

  .course .course-item {
    width: 1050px;
    background: #fff;
    padding: 20px 30px 20px 20px;
    margin-bottom: 35px;
    border-radius: 2px;
    cursor: pointer;
    box-shadow: 2px 3px 16px rgba(0, 0, 0, 0.1);
    /* css3.0 过渡动画 hover 事件操作 */
    transition: all 0.2s ease;
  }

  .course .course-item::after {
    content: "";
    display: block;
    clear: both;
  }

  /* 顶级元素 父级元素  当前元素{} */
  .course .course-item .course-image {
    float: left;
    width: 423px;
    height: 210px;
    margin-right: 30px;
  }

  .course .course-item .course-image img {
    width: 100%;
  }

  .course .course-item .course-info {
    float: left;
    width: 596px;
  }

  .course-item .course-info h3 {
    font-size: 26px;
    color: #333;
    font-weight: normal;
    margin-bottom: 8px;
  }

  .course-item .course-info h3 span {
    font-size: 14px;
    color: #9b9b9b;
    float: right;
    margin-top: 14px;
  }

  .course-item .course-info h3 span img {
    width: 11px;
    height: auto;
    margin-right: 7px;
  }

  .course-item .course-info .teather-info {
    font-size: 14px;
    color: #9b9b9b;
    margin-bottom: 14px;
    padding-bottom: 14px;
    border-bottom: 1px solid #333;
    border-bottom-color: rgba(51, 51, 51, 0.05);
  }

  .course-item .course-info .teather-info span {
    float: right;
  }

  .course-item .lesson-list::after {
    content: "";
    display: block;
    clear: both;
  }

  .course-item .lesson-list li {
    float: left;
    width: 44%;
    font-size: 14px;
    color: #666;
    padding-left: 22px;
    /* background: url("路径") 是否平铺 x轴位置 y轴位置 */
    background: url("/static/image/play-icon-gray.svg") no-repeat left 4px;
    margin-bottom: 15px;
  }

  .course-item .lesson-list li .lesson-title {
    /* 以下3句，文本内容过多，会自动隐藏，并显示省略符号 */
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
    display: inline-block;
    max-width: 200px;
  }

  .course-item .lesson-list li:hover {
    background-image: url("/static/image/play-icon-yellow.svg");
    color: #ffc210;
  }

  .course-item .lesson-list li .free {
    width: 34px;
    height: 20px;
    color: #fd7b4d;
    vertical-align: super;
    margin-left: 10px;
    border: 1px solid #fd7b4d;
    border-radius: 2px;
    text-align: center;
    font-size: 13px;
    white-space: nowrap;
  }

  .course-item .lesson-list li:hover .free {
    color: #ffc210;
    border-color: #ffc210;
  }

  .course-item .pay-box::after {
    content: "";
    display: block;
    clear: both;
  }

  .course-item .pay-box .discount-type {
    padding: 6px 10px;
    font-size: 16px;
    color: #fff;
    text-align: center;
    margin-right: 8px;
    background: #fa6240;
    border: 1px solid #fa6240;
    border-radius: 10px 0 10px 0;
    float: left;
  }

  .course-item .pay-box .discount-price {
    font-size: 24px;
    color: #fa6240;
    float: left;
  }

  .course-item .pay-box .original-price {
    text-decoration: line-through;
    font-size: 14px;
    color: #9b9b9b;
    margin-left: 10px;
    float: left;
    margin-top: 10px;
  }

  .course-item .pay-box .buy-now {
    width: 120px;
    height: 38px;
    background: transparent;
    color: #fa6240;
    font-size: 16px;
    border: 1px solid #fd7b4d;
    border-radius: 3px;
    transition: all 0.2s ease-in-out;
    float: right;
    text-align: center;
    line-height: 38px;
  }

  .course-item .pay-box .buy-now:hover {
    color: #fff;
    background: #ffc210;
    border: 1px solid #ffc210;
  }

  .pagein {
    text-align: center;
    margin-bottom: 20px;
  }
</style>
