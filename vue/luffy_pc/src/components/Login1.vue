<template>
  <div class="login box">
    <img src="/static/img/Loginbg.3377d0c.jpg" alt />
    <div class="login">
      <div class="login-title">
        <img src="/static/img/Logotitle.1ba5466.png" alt />
        <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
      </div>
      <div class="login_box">
        <div class="title">
          <span :class="login_type==0?'current':''" @click="login_type=0">密码登录</span>
          <span :class="login_type==1?'current':''" @click="login_type=1">短信登录</span>
        </div>
        <div class="inp" v-if="login_type==0">
          <input v-model="username" type="text" placeholder="用户名 / 手机号码" class="user" />
          <input v-model="password" type="password" name class="pwd" placeholder="密码" />
          <div id="geetest1"></div>
          <div class="rember">
            <p>
              <input type="checkbox" class="no" v-model="remember" />
              <span>记住密码</span>
            </p>
            <p>忘记密码</p>
          </div>
          <button class="login_btn" @click="get_geetest">登录</button>
          <p class="go_login">
            没有账号
            <span>立即注册</span>
          </p>
        </div>
        <div class="inp" v-show="login_type==1">
          <input v-model="username" type="text" placeholder="手机号码" class="user" />
          <input v-model="password" type="text" class="pwd" placeholder="短信验证码" />
          <button id="get_code">获取验证码</button>
          <button class="login_btn">登录</button>
          <p class="go_login">
            没有账号
            <span>立即注册</span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      login_type: 0,
      remember: false,
      username: "",
      password: ""
    };
  },

  methods: {
    get_login_user() {
      this.$axios
        .post(`${this.$settings.Host}/users/login/`, {
          username: this.username,
          password: this.password
        })
        .then(response => {
          if (this.remember) {
            //记住密码  保存daolocalstorage中
            // localStorage.setItem({
            //   username: response.data.username,
            //   token: response.data.token
            // });
            localStorage.username = response.data.username;
            localStorage.token = response.data.token;
            sessionStorage.removeItem("username");
            sessionStorage.removeItem("token");
          } else {
            // sessionStorage.setItem({
            //   username: response.data.username,
            //   token: response.data.token
            // });
            sessionStorage.username = response.data.username;
            sessionStorage.token = response.data.token;
            localStorage.removeItem("username");
            localStorage.removeItem("token");
          }
          let self = this;
          self.$alert(`欢迎登陆回来！`, `路飞学城`, {
            callback() {
              // 返回上一页
              self.$router.go(-1);
            }
          });
        })
        .catch(error => {
          this.$message.error("登陆失败");
        });
    },

    get_geetest() {
      this.$axios
        .get(`${this.$settings.Host}/users/geetest/`)
        .then(response => {
          let geetestdata = response.data;
          console.log(geetestdata);
          initGeetest(
            {
              // 省略必须的配置参数
              product: "popup",
              // area: "#area", // **必填参数**
              // next_width: "300px",
              // bg_color: "black",
              gt: geetestdata.gt,
              challenge: geetestdata.challenge,
              // new_captcha: geetestdata.new_captcha,
              offline: !geetestdata.success
            },
            this.handlerPopup
          );
        })
        .catch(error => {
          this.$message.error("获取验证码错误！");
        });
    },
    handlerPopup(captchaObj) {
      let self = this;
      console.log('12312');
      console.log(captchaObj);  
      
      captchaObj.onSuccess(function() {
        var validate = captchaObj.getValidate();
        self.$axios
          .post(`${self.$settings.Host}/users/geetest/`, {
            geetest_challenge: validate.geetest_challenge,
            geetest_validate: validate.geetest_validate,
            geetest_seccode: validate.geetest_seccode
          })
          .then(response => {
            // 验证码验证通过，执行登录处理
            self.loginHandle();
          })
          .catch(error => {
            self.$message.error("验证码验证错误！");
          });
      });
      // 将验证码加到id为captcha的元素里
      document.getElementById("geetest1").innerHTML = ""; // 先把原来容器中的验证码清空了，在添加新的验证码
      captchaObj.appendTo("#geetest1");
    }
    //   captchaObj.onSuccess(function() {
    //     var result = captchaObj.getValidate();
    //     self.$axios
    //       .post(`${self.$settings.Host}/users/geetest/`, {
    //         geetest_challenge: result.geetest_challenge,
    //         geetest_validate: result.geetest_validate,
    //         geetest_seccode: result.geetest_seccode,
    //       })
    //       .then(response => {
    //         // 验证码验证通过，执行登录处理
    //         console.log('1111')
    //         self.get_login_user();
    //       })
    //       .catch(error => {
    //         self.$message.error("验证码验证错误！");
    //       })
    //   });
    //   document.getElementById("geetest1").innerHTML = ""; // 先把原来容器中的验证码清空了，在添加新的验证码
    //   captchaObj.appendTo("#geetest1");
    // }
  }
};
</script>

<style scoped>
.box {
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.box img {
  width: 100%;
  min-height: 100%;
}
.box .login {
  position: absolute;
  width: 500px;
  height: 400px;
  left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -338px;
}
.login .login-title {
  width: 100%;
  text-align: center;
}
.login-title img {
  width: 190px;
  height: auto;
}
.login-title p {
  font-size: 18px;
  color: #fff;
  letter-spacing: 0.29px;
  padding-top: 10px;
  padding-bottom: 50px;
}
.login_box {
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
}
.login_box .title {
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: 0.32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 50px 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}
.login_box .title span.current {
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp {
  width: 350px;
  margin: 0 auto;
}
.inp input {
  outline: 0;
  width: 100%;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}
.inp input.user {
  margin-bottom: 16px;
}
.inp .rember {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-top: 10px;
}
.inp .rember p:first-of-type {
  font-size: 12px;
  color: #4a4a4a;
  letter-spacing: 0.19px;
  margin-left: 22px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  /*position: relative;*/
}
.inp .rember p:nth-of-type(2) {
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: 0.19px;
  cursor: pointer;
}

.inp .rember input {
  outline: 0;
  width: 30px;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp .rember p span {
  display: inline-block;
  font-size: 12px;
  width: 100px;
  /*position: absolute;*/
  /*left: 20px;*/
}
#geetest {
  margin-top: 20px;
}
.login_btn {
  width: 100%;
  height: 45px;
  background: #84cc39;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  letter-spacing: 0.26px;
  margin-top: 30px;
}
.inp .go_login {
  text-align: center;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: 0.26px;
  padding-top: 20px;
}
.inp .go_login span {
  color: #84cc39;
  cursor: pointer;
}
</style>