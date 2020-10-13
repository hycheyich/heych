import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Login from '../components/Login'
import Register from '../components/Register'
import Course from '../components/Course'
import Detail from '../components/Detail'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      name: "Home",
      path: "/home",
      component: Home,
    },
    {
      name: "login",
      path: "/user/login",
      component: Login,
    },
    {
      name: 'register',
      path: '/register',
      component: Register
    },
    {
      name: 'courses',
      path: '/courses',
      component: Course
    },
    {
      name: 'detial',
      path: '/courses/:id',
      component: Detail
    },
    {
      name: 'cart',
      path: '/cart',
      component: ()=>import('../components/Cart')
    },
    {
      name:'order',
      path:'/buy',
      component: ()=>import('../components/Order')
    }
  ]
})
