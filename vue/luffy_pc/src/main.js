// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App' 
import router from './router'
import axios from 'axios'

// 允许ajax发送请求时附带cookie
axios.defaults.withCredentials = false
Vue.prototype.$axios = axios;


import settings from './settings'
Vue.prototype.$settings = settings;
import ElementUI from 'element-ui'
Vue.use(ElementUI)

import "../static/css/reset.css";
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
