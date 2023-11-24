import { createRouter, createWebHistory } from 'vue-router'
// import Home from '@/views/Home.vue'
// import About from '@/views/About.vue'
// import Manage from '@/views/Manage.vue'
// import Song from '@/views/Song.vue'

import loginPage from '../components/loginPage.vue'
import signupPage from '../components/signupPage.vue'
import registrationformPage from '../components/registrationformPage.vue'
import messagePage from '../components/messagePage.vue'
import homePage from '@/views/homePage.vue'
import profilePage from '../components/profilePage.vue'
import userviewPage from '../components/userviewPage.vue'
import commentsPage from '../components/commentPage.vue'
import notificationsPage from '../components/notificationPage.vue'
// import homePag from '@/components/homePage.vue'


const routes = [
  {
    name: 'login',
    path: '/login',
    component: loginPage
  },
  {
    name: 'comments',
    path: '/comment/:tweetId/',
    component: commentsPage
  },
  {
    name: 'profile',
    path: '/profile',
    component: profilePage
  },
  {
    name: 'message',
    path: '/message',
    component: messagePage
  },
  {
    name: 'userview',
    path: '/userview/:userId/:username',
    component: userviewPage
  },
  {
    name: 'signup',
    path: '/',
    component: signupPage
  },
  {
    name: 'register',
    path: '/register',
    component: registrationformPage
  },
  {
    name: 'home',
    path: '/home',
    component: homePage
  },
  {
    name: 'notification',
    path: '/notification',
    component: notificationsPage
  },

//   {
//     name: 'manage',
//     // alias: "/manage",
//     path: '/manage-music',
//     component: Manage,
//     beforeEnter(to, from, next) {
//       console.log('Manage Route Guard')
//       next()
//     },
//     meta: {
//       requiresAuth: true
//     }
//   },
//   {
//     path: '/manage',
//     redirect: { name: 'manage' }
//   },
//   {
//     path: '/:catchAll(.*)*',
//     redirect: { name: 'home' }
//   }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  linkExactActiveClass: 'text-yellow-500'
})



// Create the router guard
router.beforeEach((to, from, next) => {
  const allowedPaths = ['/login', '/', '/register'];

  if (allowedPaths.includes(to.path)) {
    // Allow access to /login and /sign paths and /register path
    next();
  } else {
    // Check if the user is logged in
    const token = sessionStorage.getItem('token');
    const user_id = sessionStorage.getItem('user_id')
    const username = sessionStorage.getItem('username')

    if (token || user_id || username) {
      // User is logged in, allow access to the requested route
      next();
    } else {
      // User is not logged in, redirect to the login page
      next('/login');
    }
  }
});


export default router
