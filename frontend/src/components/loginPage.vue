<template>
    <div class="bg-gray-500 w-full  flex flex-col ">
        <div class="bg-slate-900 mt-11 pt-16 ml-96 mb-10 flex flex-col mr-96 rounded-lg">
                <img class="w-11 rounded-3xl ml-72" src="../../public/twitterlogo.jpeg" alt="">
                <h2 class="text-white text-xl ml-60 mt-4 font-bold"> Sign in to Twitter </h2><br>
         
                <!-- <button type="button" class="ml-56 mr-80 text-white bg-[#3b5998] hover:bg-[#3b5998]/90 focus:ring-4 focus:outline-none focus:ring-[#3b5998]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#3b5998]/55 mr-2 mb-2">
                    <svg class="w-4 h-4 mr-2 -ml-1" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="facebook-f" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M279.1 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.4 0 225.4 0c-73.22 0-121.1 44.38-121.1 124.7v70.62H22.89V288h81.39v224h100.2V288z"></path></svg>
                    Sign in with Facebook
                </button> -->

                
                 <!-- <button type="button" class="ml-56 mr-80 mt-3 text-white bg-[#4285F4] hover:bg-[#4285F4]/90 focus:ring-4 focus:outline-none focus:ring-[#4285F4]/50 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-[#4285F4]/55 mr-2 mb-2">
                        <svg class="w-4 h-4 mr-2 -ml-1" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="google" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 488 512"><path fill="currentColor" d="M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4z"></path></svg>
                        Sign in with Google  
                </button> -->
                <p class="ml-80 text-white">Or </p>
                <input class="ml-56 mr-80 p-1 mt-3 px-5 py-2.5 border rounded-lg hover:rounded-full " v-model="username" type="text" placeholder="username">
                <input class="ml-56 mr-80 p-1 mt-3 px-5 py-2.5 border rounded-lg hover:rounded-full " v-model="password" type="password" placeholder="Password">

                <button @click="login" class="ml-56 mr-80 mt-4 bg-white text-black rounded-lg text-sm px-5 py-2.5 text-center font-medium hover:text-white hover:bg-black hover:rounded-full">Login</button>
                <button class="ml-56 mr-80 mt-4 bg-white text-black border-gray-50 rounded-lg text-sm px-5 py-2.5 text-center font-medium hover:text-white hover:bg-black hover:rounded-full">Forgot password?</button>

                <span class="text-white mb-20 mt-10 ml-56">Don't have an account? 
                    <span> <router-link to="/" class="font-extrabold text-blue-500 hover:text-white">Sign up</router-link>
                </span></span>
        </div>
    </div>

</template>
<script>
import axios from 'axios'

import {  useUserTokenStore } from '@/stores/userToken.js'

  
// import { mapState } from 'pinia'
// import { mapWritableState } from 'pinia'
// import {useUserStore} from '@/stores/user.js'

export default {
  setup() {
        const userTokenStore = useUserTokenStore()
        const user_token = userTokenStore.user_token
        return {
          user_token
    }
  },
  data() {
    return {
      tab: 'login',
      email: null,
      username: null,
      password: null,
      showModal: false,
      success: null,
      userdata: [],
     
    }

  },
  // computed:{
  //   ...mapWritableState(userModelstore, ['user_id'])
  // },

  methods: {
    setAuthToken(token) {
          if (token) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          } else {
            delete axios.defaults.headers.common['Authorization'];
          }
    },
    login() {
      const formData = {
        username: this.username,
        password: this.password
      }
      axios
        .post('http://127.0.0.1:8000/api/v1/login/', formData)
        .then((response) => {
          console.log(response.data.message)

          this.success = 'Successfull LoggedIn!'

          const token = response.data.token
          console.log(token)

          this.userdata = response.data.user_data
          // console.log(this.userdata)
          const user_id = this.userdata.id
          const username = this.userdata.username

          localStorage.setItem('token',token );
          localStorage.setItem('user_id',user_id );
          localStorage.setItem('username',username );

          
          this.setAuthToken(token);
          
          // const userTokenStore = useUserTokenStore()
          // userTokenStore.setUserToken(response.data.token)

          // console.log(userTokenStore)

          // this.user_id = response.data.user_id
          // console.log(userStore.user_id)

          this.$router.push('/home')

        })
        .catch((error) => {
          console.error(error.response.data.message)
          // Handle login error
        })
    },
    closeModal() {
      this.showModal = false
      console.log('closeModal')
    }
  }
}
</script>


