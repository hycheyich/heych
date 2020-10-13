<template>
  <div class="cart">
    <Header/>
    <div class="cart-info">
      <h3 class="cart-top">购物车结算 <span>共{{course_list.length}}门课程</span></h3>
      <div class="cart-title">
        <el-row>
          <el-col :span="2">&nbsp;</el-col>
          <el-col :span="10">课程</el-col>
          <el-col :span="8">有效期</el-col>
          <el-col :span="4">价格</el-col>
        </el-row>
      </div>
      <div class="cart-item" v-for="(course,kk) in course_list" :key="kk">
        <el-row>
          <el-col :span="2" class="checkbox">&nbsp;&nbsp;</el-col>
          <el-col :span="10" class="course-info">
            <img src="/static/img/course-cover.jpeg" alt="">
            <span class="course-title">{{course.course_name}}<br>限时免费</span>
          </el-col>
          <el-col :span="8"><span>{{course.expire_text}}</span></el-col>
          <el-col :span="4" class="course-price">¥{{parseFloat(course.discount_price).toFixed(2)}}<br><span>原价 ¥{{parseFloat(course.original_price).toFixed(2)}}</span>
          </el-col>
        </el-row>
      </div>
      <div class="discount">
        <div id="accordion">
          <div class="coupon-box">
            <div class="icon-box">
              <span class="select-coupon">使用优惠劵：</span>
              <a class="select-icon" @click="use_coupon=!use_coupon"><img class="sign"
                                                                          :class="use_coupon?'is_show_select':''"
                                                                          src="../../static/img/12.png" alt=""></a>
              <span class="coupon-num">有3张可用</span>
            </div>
            <p class="sum-price-wrap">商品总金额：<span class="sum-price">{{total_price.toFixed(2)}}元</span></p>
          </div>
          <div id="collapseOne" v-if="use_coupon">
            <ul class="coupon-list" v-if="coupon_list.length>0">
              <li class="coupon-item"
                  :class="{disable:total_price<item.coupon.condition || check_duration(item.start_time,item.coupon.duration),active:coupon==item.id}"
                  @click="select_coupon(item)" :key="key" v-for="item,key in coupon_list">
                <p class="coupon-name">{{item.coupon.name}}</p>
                <p class="coupon-condition" v-if="item.coupon.condition>0">满{{item.coupon.condition}}元可以使用</p>
                <p class="coupon-time start_time">开始时间：{{item.start_time.replace("T"," ")}}</p>
                <p class="coupon-time end_time">过期时间：{{get_end_time(item.start_time,item.coupon.duration)}}</p>
              </li>
            </ul>
            <div class="no-coupon" v-else>
              <span class="no-coupon-tips">暂无可用优惠券</span>
            </div>
          </div>
        </div>
        <div class="credit-box" v-if="total_real_price>0">
          <label class="my_el_check_box">
            <el-checkbox class="my_el_checkbox" v-model="use_credit"></el-checkbox>
          </label>
          <p class="discount-num1" v-if="!use_credit">使用我的贝里</p>
          <p class="discount-num2" v-if="use_credit"><span>总积分：12000，已抵扣 ￥0，本次花费0积分</span></p>
        </div>
        <p class="sun-coupon-num">优惠券抵扣：<span>0.00元</span></p>
      </div>
      <div class="calc">
        <el-row class="pay-row">
          <el-col :span="4" class="pay-col"><span class="pay-text">支付方式：</span></el-col>
          <el-col :span="8">
            <span class="alipay" @click="pay_type=1" v-if="pay_type!=1"><img src="../../static/img/alipay.png"
                                                                             alt="支付宝"></span>
            <span class="alipay" v-if="pay_type==1"><img src="../../static/img/alipay2.png" alt="支付宝"></span>
            <span class="alipay wechat" @click="pay_type=2" v-if="pay_type!=2"><img src="../../static/img/wechat.png"
                                                                                    alt="微信支付"></span>
            <span class="alipay wechat" v-if="pay_type==2"><img src="../../static/img/wechat2.png" alt="微信支付"></span>
          </el-col>
          <el-col :span="8" class="count">实付款： <span>¥{{total_real_price}}</span></el-col>
          <el-col :span="4" class="cart-pay"><span @click="payhander">立即支付</span></el-col>
        </el-row>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Footer from "./common/Footer"

  export default {
    name: "Order",
    data() {
      return {
        course_list: [],     // 勾选商品列表
        total_price: 0,      // 课程总价
        total_real_price: 0, // 实付总价
        use_coupon: false, // 是否使用优惠券
        use_credit: false, // 是否使用积分
        coupon_list: [],    // 用户的优惠券列表
        coupon: 0,   // 当前用户选择的优惠券ID
        coupon_price: 0, // 优惠券抵扣价格
        my_credit: 0, // 用户拥有的积分
        current_credit: 0,       // 本次订单可以使用的积分
        credit_rmb: 0, // 积分兑换比率
        credit_price: 0,  // 积分折算价格
        pay_type: 1,  // 支付方式,
        token: "",
      }
    },
    components: {
      Header,
      Footer,
    },
    created() {
      this.check_user_login();
      this.get_selected_course();
    },

    methods: {
      check_user_login() {
        // 检查是否登陆
        this.token = this.$settings.token();
        if (!this.token) {
          this.$confirm('对不起，您尚未登录请登录后继续操作, 是否继续?', '路飞学城', {
            confirmButtonText: '登录',
            cancelButtonText: '返回上一页',
            type: 'error'
          }).then(() => {
            this.$router.push("/user/login");
          }).catch(() => {
            this.$router.go(-1);
          });
          return false; // 阻止代码继续往下执行
        }
      },
      get_selected_course() {
        // 获取购物车中勾选的商品信息

        this.$axios.get(`${this.$settings.Host}/cart/selected/`,
          {
            headers: {
              Authorization: "jwt " + this.token,
            }
          }
        ).then(response => {
          this.course_list = response.data;
          let total_price = 0;
          for (let course of this.course_list) {
            total_price += course.discount_price;
          }
          this.total_price = total_price;
        }).catch(error => {
          this.$message.error("对不起，获取购物车商品失败！");

        })
      },
      payhander() {
        //   发起生成订单请求
        this.$axios.post(`${this.$settings.Host}/orders/`, {
          credit: this.current_credit,
          coupon: this.coupon,
          pay_type: this.pay_type
        }, {
          headers: {
            Authorization: "jwt " + this.token,
          }
        }).then(response => {
          // 直接跳转到支付页面

        }).catch(error => {
          this.$message.error("生成订单失败！");
        })
      },
    },
  }
</script>

<style scoped>
  .cart {
    /*margin-top: 80px;*/
  }

  .cart-info {
    overflow: hidden;
    width: 1200px;
    margin: auto;
  }

  .cart-top {
    font-size: 18px;
    color: #666;
    margin: 25px 0;
    font-weight: normal;
  }

  .cart-top span {
    font-size: 12px;
    color: #d0d0d0;
    display: inline-block;
  }

  .cart-title {
    background: #F7F7F7;
    height: 70px;
    line-height: 70px;
  }

  .calc {
    margin-top: 25px;
    margin-bottom: 40px;
  }

  .calc .count {
    text-align: right;
    margin-right: 10px;
    vertical-align: middle;
  }

  .calc .count span {
    font-size: 36px;
    color: #333;
  }

  .calc .cart-pay {
    margin-top: 5px;
    width: 110px;
    height: 38px;
    outline: none;
    border: none;
    color: #fff;
    line-height: 38px;
    background: #ffc210;
    border-radius: 4px;
    font-size: 16px;
    text-align: center;
    cursor: pointer;
  }

  .cart-item {
    height: 120px;
    line-height: 120px;
    margin-top: 30px;
    margin-bottom: 30px;
  }

  .course-info img {
    width: 175px;
    height: 115px;
    margin-right: 35px;
    vertical-align: middle;
    float: left;
  }

  .course-title {
    float: left;
    line-height: 32px;
    margin-top: 26px;
  }

  .course-price {
    line-height: 32px;
    margin-top: 32px;
  }

  .course-price span {
    text-decoration: line-through;
    color: #5e5e5e;
  }

  .alipay {
    display: inline-block;
    height: 48px;
    cursor: pointer;
  }

  .alipay img {
    height: 100%;
    width: auto;
  }

  .pay-text {
    display: block;
    text-align: right;
    height: 100%;
    line-height: 100%;
    vertical-align: middle;
    margin-top: 20px;
  }

  .discount {
    text-align: right;
    margin-top: 30px;
  }

  .coupon-box {
    text-align: left;
    padding-bottom: 22px;
    padding-left: 30px;
    border-bottom: 1px solid #e8e8e8;
  }

  .coupon-box::after {
    content: "";
    display: block;
    clear: both;
  }

  .icon-box {
    float: left;
  }

  .icon-box .select-coupon {
    float: left;
    color: #666;
    font-size: 16px;
  }

  .icon-box::after {
    content: "";
    clear: both;
    display: block;
  }

  .select-icon {
    width: 20px;
    height: 20px;
    float: left;
  }

  .select-icon img {
    max-height: 100%;
    max-width: 100%;
    margin-left: 10px;
    margin-top: 2px;
    transform: rotate(-90deg);
    transition: transform .5s;
  }

  .is_show_select {
    transform: rotate(0deg) !important;
  }

  .coupon-num {
    height: 22px;
    line-height: 22px;
    padding: 0 5px;
    text-align: center;
    font-size: 12px;
    float: left;
    color: #fff;
    letter-spacing: .27px;
    background: #fa6240;
    border-radius: 2px;
    margin-left: 20px;
  }

  .sum-price-wrap {
    float: right;
    font-size: 16px;
    color: #4a4a4a;
    margin-right: 45px;
  }

  .sum-price-wrap .sum-price {
    font-size: 18px;
    color: #fa6240;
  }

  .no-coupon {
    text-align: center;
    width: 100%;
    padding: 50px 0px;
    align-items: center;
    justify-content: center; /* 文本两端对其 */
    border-bottom: 1px solid rgb(232, 232, 232);
  }

  .no-coupon-tips {
    font-size: 16px;
    color: #9b9b9b;
  }

  .credit-box {
    height: 30px;
    margin-top: 40px;
    display: flex;
    align-items: center;
    justify-content: flex-end
  }

  .my_el_check_box {
    position: relative;
  }

  .my_el_checkbox {
    margin-right: 10px;
    width: 16px;
    height: 16px;
  }

  .discount-num1 {
    color: #9b9b9b;
    font-size: 16px;
    margin-right: 45px;
  }

  .discount-num2 {
    margin-right: 45px;
    font-size: 16px;
    color: #4a4a4a;
  }

  .sun-coupon-num {
    margin-right: 45px;
    margin-bottom: 43px;
    margin-top: 40px;
    font-size: 16px;
    color: #4a4a4a;
    display: inline-block;
  }

  .sun-coupon-num span {
    font-size: 18px;
    color: #fa6240;
  }

  .coupon-list {
    margin: 20px 0;
  }

  .coupon-list::after {
    display: block;
    content: "";
    clear: both;
  }

  .coupon-item {
    float: left;
    margin: 15px 8px;
    width: 180px;
    height: 100px;
    padding: 5px;
    background-color: #fa3030;
    cursor: pointer;
  }

  .coupon-list .active {
    background-color: #fa9000;
  }

  .coupon-list .disable {
    cursor: not-allowed;
    background-color: #fa6060;
  }

  .coupon-condition {
    font-size: 12px;
    text-align: center;
    color: #fff;
  }

  .coupon-name {
    color: #fff;
    font-size: 24px;
    text-align: center;
  }

  .coupon-time {
    text-align: left;
    color: #fff;
    font-size: 12px;
  }
</style>
