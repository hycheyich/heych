<template>
  <div class="footer">
    <el-container>
      <el-row>
        <el-col :span="4" v-for="(footer,key) in nav_footer_list" :key="key">
          <a :href="footer.link" >{{footer.name}}</a>
        </el-col>
        <el-col :span="24" class="banquan">
          <p class="copyright">Copyright © luffycity.com版权所有 | 京ICP备17072161号-1</p>
        </el-col>
      </el-row>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      nav_footer_list: []
    };
  },
  created () {
    this.get_nav_footer_list();
  },
  methods: {
    get_nav_footer_list() {
      this.$axios
        .get(`${this.$settings.Host}/nav/footer`)
        .then(response => {
          this.nav_footer_list = response.data;
        })
        .catch(error => {
          this.$message.error("底部导航显示失败");
        });
    }
  }
};
</script>

<style scoped>
.footer {
  width: 100%;
  height: 128px;
  background: #25292e;
}
.footer .el-container {
  width: 1200px;
  margin: auto;
}
.footer .el-row {
  align-items: center;
  padding: 0 200px;
  padding-bottom: 15px;
  width: 100%;
  margin-top: 38px;
}
.footer .el-row a {
  color: #fff;
  font-size: 14px;
}
.footer .el-row .copyright {
  text-align: center;
  color: #fff;
  font-size: 14px;
}
.banquan{
  margin-top: 20px
}

</style>
