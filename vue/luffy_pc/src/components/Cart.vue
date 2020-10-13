<template>
  <div class="cart">
    <Header></Header>
    <div class="cart_info">
      <div class="cart_title">
        <span class="text">我的购物车</span>
        <span class="total">共{{course_list.length}}门课程</span>
      </div>
      <div class="cart_table">
        <div class="cart_head_row">
          <span class="doing_row"></span>
          <span class="course_row">课程</span>
          <span class="expire_row">有效期</span>
          <span class="price_row">单价</span>
          <span class="do_more">操作</span>
        </div>
        <div class="cart_course_list">
          <CartItem v-for="(course,k) in course_list" :key="k" :course="course" :user_token="user_token" :course_key="k"
                    @del_cart="del_cart" :select_all="select_all" :comput="compute_total"></CartItem>
        </div>
        <div class="cart_footer_row">
          <span class="cart_select"><label> <el-checkbox
            v-model="select_all"></el-checkbox><span>全选</span></label></span>
          <span class="cart_delete"><i class="el-icon-delete"></i> <span>删除</span></span>
          <!--          <span class="goto_pay">去结算</span>-->
          <span class="goto_pay"><router-link to="/buy">去结算</router-link></span>
          <span class="cart_total">总计：¥ {{total.toFixed(2)}}</span>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Footer from "./common/Footer"
  import CartItem from "./common/CartItem"

  export default {
    name: "Cart",
    data() {
      return {
        checked: false,
        user_token: '',
        course_list: [],
        select_all: false,
        total: 0,
      }
    },
    created() {
      this.checking_login_status();

      // 获取购物车商品列表
      this.get_cart();
    },
    watch: {
      'select_all'(newValue, oldValue) {
        this.$axios.put(`${this.$settings.Host}/cart/`,
          {
            course_id: this.course_list,
            selected: this.select_all
          },
          {
            headers: {
              'Authorization': 'jwt ' + this.user_token
            }
          }
        ).then(respons => {
          this.compute_total();
        }).catch(error => {
          this.$message.error("切换勾选状态失败！");
        })
      },
    },
    methods: {
      get_cart() {
        // 获取购物车商品
        // 获取购物车商品时先判断是否登陆
        if (!this.user_token) {
          return false;
        }
        this.$axios.get(`${this.$settings.Host}/cart/`, {
          headers: { // 访问需要登录认证权限的api接口必须附带token到请求头中
            "Authorization": "jwt " + this.user_token,
          }
        }).then(response => {
          this.course_list = response.data;
          this.compute_total();
        }).catch(error => {
          this.$message.error("无法获取购物车商品列表，请联系客服工作人员！");
        })
      },
      checking_login_status() {
        //判断是否获取token
        this.user_token = this.$settings.token();
        if (!this.user_token) {
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
      del_cart(key) {
        // 前端删除
        this.course_list.splice(key, 1);
        this.compute_total();
      },
      compute_total() {
        //  计算总额
        let total = 0;
        for (let course of this.course_list) {
          if (course.selected) {
            total += parseFloat(course.price)
          }
        }
        this.total = total;
      }
    },
    components: {
      Header,
      Footer,
      CartItem,
    }
  }
</script>

<style scoped>
  .cart_info {
    width: 1200px;
    margin: 0 auto 200px;
  }

  .cart_title {
    margin: 25px 0;
  }

  .cart_title .text {
    font-size: 18px;
    color: #666;
  }

  .cart_title .total {
    font-size: 12px;
    color: #d0d0d0;
  }

  .cart_table {
    width: 1170px;
  }

  .cart_table .cart_head_row {
    background: #F7F7F7;
    width: 100%;
    height: 80px;
    line-height: 80px;
    padding-right: 30px;
  }

  .cart_table .cart_head_row::after {
    content: "";
    display: block;
    clear: both;
  }

  .cart_table .cart_head_row .doing_row,
  .cart_table .cart_head_row .course_row,
  .cart_table .cart_head_row .expire_row,
  .cart_table .cart_head_row .price_row,
  .cart_table .cart_head_row .do_more {
    padding-left: 10px;
    height: 80px;
    float: left;
  }

  .cart_table .cart_head_row .doing_row {
    width: 78px;
  }

  .cart_table .cart_head_row .course_row {
    width: 530px;
  }

  .cart_table .cart_head_row .expire_row {
    width: 188px;
  }

  .cart_table .cart_head_row .price_row {
    width: 162px;
  }

  .cart_table .cart_head_row .do_more {
    width: 162px;
  }

  .cart_footer_row {
    padding-left: 30px;
    background: #F7F7F7;
    width: 100%;
    height: 80px;
    line-height: 80px;
  }

  .cart_footer_row .cart_select span {
    font-size: 18px;
    color: #666;
  }

  .cart_footer_row .cart_delete {
    margin-left: 58px;
  }

  .cart_delete .el-icon-delete {
    font-size: 18px;
  }

  .cart_delete span {
    margin-left: 15px;
    cursor: pointer;
    font-size: 18px;
    color: #666;
  }

  .cart_total {
    float: right;
    margin-right: 62px;
    font-size: 18px;
    color: #666;
  }

  .goto_pay {
    float: right;
    width: 159px;
    height: 80px;
    outline: none;
    border: none;
    background: #ffc210;
    font-size: 18px;
    color: #fff;
    text-align: center;
    cursor: pointer;
  }
</style>
