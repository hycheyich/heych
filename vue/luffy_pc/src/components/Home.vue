<template>
  <div>
    <div class="home">
        <!-- 头部 -->
      <Header></Header>
      <!-- 导航栏 -->
      <Banner></Banner>
      <!-- 尾部 -->
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
  import Header from "./common/Header"
  import Banner from "./common/Banner"
  import Footer from "./common/Footer"
export default {
  name: "Home",
  data() {
    return {
    };
  },
  components: {
    Header,
    Footer,
    Banner,
  }
};
</script>

<style  scoped>
</style>
