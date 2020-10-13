<template>
  <div class="cart_item">
    <div class="cart_column column_1">
      <el-checkbox class="my_el_checkbox" v-model="course.selected"></el-checkbox>
    </div>
    <div class="cart_column column_2">
      <img src="/static/image/course_demo.png" alt="">
      <span><router-link :to="`/courses/${course.course_id}`">{{course.course_name}}</router-link></span>
    </div>
    <div class="cart_column column_3">
      <el-select v-model="course.expire" size="mini" placeholder="请选择购买有效期" class="my_el_select">
        <el-option :label="course_expire.text" :key="kk" :value='course_expire.expire'
                   v-for="(course_expire,kk) in course.expire_list"></el-option>
      </el-select>
    </div>
    <div class="cart_column column_4">{{course.price.toFixed(2)}}</div>
    <div class="cart_column column_4"><span class="del" @click="deleteHandle">删除</span></div>
  </div>
</template>

<script>
  export default {
    name: "CartItem",
    props: ['course', 'user_token', 'course_key', 'select_all','comput'],
    data() {
      return {
        checked: false,
        expire: "1个月有效",
      }
    },
    watch: {
      'course.selected'(newValue, oldValue) {
        // 监听课程勾选
        this.change_selectd();
        this.comput();
      },
      'select_all'() {
        // 监听全选按钮
        this.course.selected = this.select_all;
      },
      'course.expire'() {
        //  监听课程有效期状态
        console.log(this.course.expire);
        this.change_course_expire()
      }
    },


    methods: {
      //删除提示
      // delete_prompt() {
      //
      //   this.$confirm('是否删除购物车中此商品？', '确认删除', {
      //     distinguishCancelAndClose: true,
      //     confirmButtonText: '确定',
      //     cancelButtonText: '取消'
      //   }).then(() => {
      //     this.$message.info('正在删除此商品，请等待')
      //
      //   }).catch(() => {
      //     this.$message.info('商品未删除'
      //     )
      //   })
      // },
      change_selectd() {
        //改变勾选状态
        this.$axios.put(`${this.$settings.Host}/cart/`,
          {
            course_id: this.course.course_id,
            selected: this.course.selected
          },
          {
            headers: {
              'Authorization': 'jwt ' + this.user_token
            }
          }
        ).then(respons => {
          // this.$message.success("切换勾选状态成功！");
        }).catch(error => {
          this.$message.error("切换勾选状态失败！");
        })
      },
      deleteHandle() {
        //删除商品
        this.$confirm('是否删除购物车中此商品？', '确认删除', {
          distinguishCancelAndClose: true,
          confirmButtonText: '确定',
          cancelButtonText: '取消'
        }).then(() => {
          this.$message.info('正在删除此商品，请等待')
          this.$axios.delete(`${this.$settings.Host}/cart/`, {
            params: {
              course_id: this.course.course_id,
            },
            headers: {
              'Authorization': 'jwt ' + this.user_token
            }
          }).then(response => {
            this.$message.success(response.data.message);
            this.$emit("del_cart", this.course_key);
          }).catch(error => {
            this.$message.error('删除数据失败')
          })
        }).catch(() => {
          this.$message.info('商品未删除'
          )
        })
      },
      change_course_expire() {
        // 切换商品的有效期
        for (let item of this.course.expire_list) {
          if (this.course.expire === item.expire) {
            //  表示永久有效
            // console.log(this.course.expire);
            // todo 存在bug 存储有效期失败，发送有效期失败
            this.course.price = item.price;
            this.$axios.patch(`${this.$settings.Host}/cart/`,
              {
                course_id: this.course.course_id,
                expire_id: this.course.expire,
              },
              {
                headers: {
                  'Authorization':
                    'jwt ' + this.user_token
                }
              }
            ).then(response => {

            }).catch(error => {
              this.$message.error("当前课程的有效期选项切换失败！");
            })
          }
        }

      }
    }

  }
</script>

<style scoped>
  .cart_item::after {
    content: "";
    display: block;
    clear: both;
  }

  .cart_column {
    float: left;
    height: 250px;
  }

  .cart_item .column_1 {
    width: 88px;
    position: relative;
  }

  .my_el_checkbox {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    top: 0;
    margin: auto;
    width: 16px;
    height: 16px;
  }

  .cart_item .column_2 {
    padding: 67px 10px;
    width: 520px;
    height: 116px;
  }

  .cart_item .column_2 img {
    width: 175px;
    height: 115px;
    margin-right: 35px;
    vertical-align: middle;
  }

  .cart_item .column_3 {
    width: 197px;
    position: relative;
    padding-left: 10px;
  }

  .my_el_select {
    width: 117px;
    height: 28px;
    position: absolute;
    top: 0;
    bottom: 0;
    margin: auto;
  }

  .cart_item .column_4 {
    padding: 67px 10px;
    height: 116px;
    width: 142px;
    line-height: 116px;
  }

  .cart_item .column_4 .del {
    color: #ffc210;
  }

</style>
