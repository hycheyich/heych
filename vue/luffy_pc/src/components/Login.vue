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
          <button class="login_btn" @click="get_verify">登录</button>
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
      username: "",
      password: "",
      remember: false // 是否记住密码
    };
  },

  methods: {
    loginHandle() {
      // 登陆处理
      this.$axios
        .post(`${this.$settings.Host}/users/login/`, {
          username: this.username,
          password: this.password
        })
        .then(response => {
          // 登陆成功
          if (this.remember) {
            // 记住密码
            localStorage.username = response.data.username;
            localStorage.token = response.data.token;
            sessionStorage.removeItem("username");
            sessionStorage.removeItem("token");
          } else {
            // 不记住密码
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
          // 登陆失败
          document.getElementById("geetest1").innerHTML = "";
          this.$message.error("对不起，账号或密码错误！");
        });
    },
    // get_geetest_capcha(){
    //     // 获取验证码
    //     this.$axios.get(`${this.$settings.Host}/users/geetest/`).then(response=>{
    //         // 使用initGeetest接口
    //         // 参数1：配置参数
    //         // 参数2：回调，回调的第一个参数验证码对象，之后可以使用它做appendTo之类的事件
    //         let data = response.data;
    //         console.log(data);
    //         initGeetest({
    //             gt: data.gt,
    //             challenge: data.challenge,
    //             product: "popup", // 产品形式，包括：float，embed，popup。注意只对PC版验证码有效
    //             offline: !data.success, // 表示用户后台检测极验服务器是否宕机，一般不需要关注
    //             new_captcha:false
    //         }, this.handlerPopup);
    //     }).catch(error=>{
    //         this.$message.error("获取验证码错误！");
    //     });

    // },
    // handlerPopup(captchaObj){
    //     // 验证码的二次验证
    //     // 成功的回调
    //     captchaObj.appendTo("#geetest1");
    //     let self = this;
    //     console.log("111");

    // //     captchaObj.onReady(function(){
    // //     //验证码ready之后才能调用verify方法显示验证码
    // //     console.log('123');

    // // })
    //     captchaObj.onSuccess(function () {
    //         console.log('111');

    //         var validate = captchaObj.getValidate();
    //         self.$axios.post(`${self.$settings.Host}/users/geetest/`,{
    //                 geetest_challenge: validate.geetest_challenge,
    //                 geetest_validate: validate.geetest_validate,
    //                 geetest_seccode: validate.geetest_seccode
    //         }).then(response=>{
    //             // 验证码验证通过，执行登录处理
    //             self.loginHandle();
    //         }).catch(error=>{
    //             self.$message.error("验证码验证错误！");
    //         })
    //     });
    //     // 将验证码加到id为captcha的元素里
    //     document.getElementById("geetest1").innerHTML = ""; // 先把原来容器中的验证码清空了，在添加新的验证码
    //     captchaObj.appendTo("#geetest1");
    // }
    get_verify() {
      // 首先用户名和密码不能为空
      if (!this.username || !this.password) {
        this.$message.error("用户名和密码均不能为空!");
        return;
      }

      // 首先从后端获取appId
      this.$axios
        .get(`${this.$settings.Host}/users/verify/`)
        .then(response => {
          // 拿到了appId,构建验证码对象
          let appId = response.data;
          let self = this;
          // 这里其实是给这个元素绑定了一个事件
          let tct = new TencentCaptcha(
            document.getElementById("geetest1"),
            appId,
            function(res) {
              // 验证码的回调函数
              if (res.ret === 0) {
                // 票据
                let ticket = res.ticket;
                let randstr = res.randstr;
                self.check_verify(ticket, randstr);
              }
            }
          );
          // 显示验证码
          tct.show();
        })
        .catch(error => {
          this.$message.error("获取验证码出错!请联系管理员!");
        });
    },
    check_verify(ticket, randstr) {
      // 将ticket,randstr发送到后端进行验证
      this.$axios
        .post(`${this.$settings.Host}/users/verify/`, {
          ticket: ticket,
          randstr: randstr
        })
        .then(response => {
          if (response.status === 200) {
            // 校验成功, 进行登录,这里调用之前写好的登录方法
            this.loginHandle();
          } else {
            this.$message.error("校验失败!");
          }
        })
        .catch(error => {
          this.$message.error("校验验证码出错!请联系管理员!");
        });
    }
  }
};
</script>

<style scoped>
.box {
  width: 100%;
  height: 100%;
  position: relative;
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
#geetest1 {
  margin-top: 15px;
}
</style>