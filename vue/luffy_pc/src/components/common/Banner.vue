<template>
  <div class="banner">
    <el-carousel trigger="click" height="700px">
      <el-carousel-item v-for="(banner,index) in banner_list" :key="index">
        <a :href="banner.link">
          <img width="100%" height="700px" :src="banner.image" alt />
        </a>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: "Banner",
  data() {
    return {
      banner_list: []
    };
  },
  created () {
    this.get_banner_list();
  },

  methods: {
    get_banner_list() {
      this.$axios
        .get(`${this.$settings.Host}/banner`)
        .then(response => {
          this.banner_list = response.data
        })
        .catch(error => {
          this.$message.error('轮播图显示失败')
        });
    }
  }
};
</script>

<style scoped>
.el-carousel__arrow {
  width: 100px !important;
  height: 100px !important;
}
.el-icon-arrow-left {
  font-size: 35px;
  margin-left: 50px;
}
.el-carousel__arrow--left {
  left: -50px;
}
</style>
