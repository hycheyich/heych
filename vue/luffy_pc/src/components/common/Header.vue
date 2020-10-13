<template>
  <div class="header">
    <el-container>
      <div class="header-top">
        <p>老男孩IT教育 | 帮助有志向的年轻人通过努力学习获得体面的工作和生活</p>
      </div>
      <el-header>
        <el-row>
          <el-col class="logo" :span="3">
            <a href="/">
              <img src="/static/img/logo.svg" alt/>
            </a>
          </el-col>
          <el-col class="nav" :span="16">
            <el-row>
              <el-col :span="3" v-for="(nav,key) in nav_list" :key="key">
                <a :href="nav.link" v-if="nav.is_http">{{nav.name}}</a>
                <router-link :to="nav.link" class="current" v-else>{{nav.name}}</router-link>
              </el-col>
            </el-row>
          </el-col>
          <el-col class="login-bar" :span="5">
            <el-row v-show="login_sign">
              <el-col class="cart-ico" :span="9">
                <router-link to>
                  <b class="goods-number">0</b>
                  <img class="cart-icon" src alt/>
                  <span>
                    <router-link to="/cart">购物车</router-link>
                  </span>
                </router-link>
              </el-col>
              <el-col class="study" :span="8" :offset="2">
                <router-link to>学习中心</router-link>
              </el-col>
              <el-col class="member remenber" :span="5">
                <el-menu class="el-menu-demo" mode="horizontal">
                  <el-submenu index="2">
                    <template slot="title">
                      <router-link to>
                        <img src="/static/img/logo@2x.png" alt/>
                      </router-link>
                      <!-- 个人中心 -->
                    </template>
                    <el-menu-item index="2-1">我的账户</el-menu-item>
                    <el-menu-item index="2-2">我的订单</el-menu-item>
                    <el-menu-item index="2-3">我的优惠卷</el-menu-item>
                    <el-menu-item index="2-3">
                      <span @click="logout">退出登录</span>
                    </el-menu-item>
                  </el-submenu>
                </el-menu>
              </el-col>
            </el-row>
            <el-row v-show="!login_sign">
              <el-col class="cart-ico" :span="9">
                <router-link to>
                  <b class="goods-number">0</b>
                  <img class="cart-icon" src alt/>
                  <span>
                    <router-link to="/cart">购物车</router-link>
                  </span>
                </router-link>
              </el-col>
              <el-col :span="10" :offset="5">
                <span class="register">
                  <router-link to="/user/login">登录</router-link>&nbsp;&nbsp;|&nbsp;&nbsp;
                  <router-link to="/register">注册</router-link>
                </span>
              </el-col>
            </el-row>
          </el-col>
        </el-row>
      </el-header>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "Header",
    data() {
      return {
        nav_list: [],
        login_sign: false,
        token: ""
      };
    },
    watch: {
      login_sign(newValue, oldValue) {
        if (!newValue) {
          this.$router.push('/home');
        }
      }
    },
    created() {
      //获取前端导航栏信息
      this.get_nav_list();
      this.chack_login();
    },
    methods: {
      get_nav_list() {
        this.$axios
          .get(`${this.$settings.Host}/nav/header/`)
          .then(response => {
            this.nav_list = response.data;
          })
          .catch(error => {
            this.$message.error("头部导航显示失败");
          });
      },
      chack_login() {
        if (localStorage.token || sessionStorage.token) {
          this.token = localStorage.token || sessionStorage.token;
          this.login_sign = true;
        }
      },
      logout() {
        this.login_sign = false;
        localStorage.removeItem("username");
        localStorage.removeItem("token");
        sessionStorage.removeItem("username");
        sessionStorage.removeItem("token");

      }
    }
  };
</script>

<style scoped>
  .header {
    top: 0;
    left: 0;
    right: 0;
    margin: 0 auto;
    background-color: #fff;
    height: 100px;
    z-index: 1000;
    position: relative;
    box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
  }

  .header .el-container {
    width: 1200px;
    margin: 0 auto;
    margin-bottom: 10px;
  }

  .header .header-top p {
    width: 1200px;
    margin: 10px auto;
    font-size: 12px;
    cursor: pointer;
    color: #9d9d9d;
  }

  .el-header {
    height: 80px !important;
    padding: 0;
  }

  .logo img {
    padding-top: 16px;
    width: 118px;
    height: auto;
    cursor: pointer;
    margin-right: 50px;
  }

  .nav {
    margin-top: 22px;
  }

  .nav .el-col a {
    display: inline-block;
    text-align: center;
    padding-bottom: 16px;
    padding-left: 5px;
    padding-right: 5px;
    position: relative;
    font-size: 16px;
    margin-left: 20px;
  }

  .nav .el-col a:hover {
    border-bottom: 4px solid #ffc210;
  }

  .nav .el-col .current {
    color: #4a4a4a;
  }

  .login-bar {
    margin-top: 22px;
  }

  .cart-ico {
    position: relative;
    border-radius: 17px;
  }

  .cart-ico:hover {
    background: #f0f0f0;
  }

  .goods-number {
    width: 16px;
    height: 16px;
    line-height: 17px;
    font-size: 12px;
    color: #fff;
    text-align: center;
    background: #fa6240;
    border-radius: 50%;
    transform: scale(0.8);
    position: absolute;
    left: 16px;
    top: -1px;
  }

  .cart-icon {
    width: 15px;
    height: auto;
    margin-left: 6px;
  }

  .cart-ico span {
    margin-left: 12px;
  }

  .member img {
    margin-top: -10px;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    display: inline-block;
  }
</style>
