<template> 
    <div class="bg-gray-500 w-full  flex flex-col ">
        <div class="bg-slate-900 mt-11 pt-16 ml-96 flex flex-col mr-96 rounded-lg">
                <img class="w-11 rounded-3xl ml-72" src="../../public/twitterlogo.jpeg" alt="">
                <h2 class="text-white text-xl ml-60 mt-4 font-bold"> Registration Form </h2><br>


                  <!-- Success message display -->
                <div id="alert-3" v-if="success" class="flex items-center p-4 mb-4 ml-40 mr-28 text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400" role="alert">              
                  <div class="ml-3 text-sm font-medium">
                    {{ success }} <a href="#" class="font-semibold underline hover:no-underline text-white">Go to login page. </a>
                </div>

                <button type="button" class="ml-auto -mx-1.5 -my-1.5 bg-green-50 text-green-500 rounded-lg focus:ring-2 focus:ring-green-400 p-1.5 hover:bg-green-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-green-400 dark:hover:bg-gray-700" data-dismiss-target="#alert-3" aria-label="Close">
                    <span class="sr-only">Close</span>
                    <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                    </svg>
                </button>
            </div>


  
                <input class="ml-56 mr-60 p-1 mt-3 px-5 py-2.5 border rounded-lg hover:rounded-full " v-model="first_name" type="text" placeholder="Name">
                <input class="ml-56 mr-60 p-1 mt-3 px-5 py-2.5 border rounded-lg hover:rounded-full " v-model="username" type="email" placeholder="Enter Username">
                <input class="ml-56 mr-60 p-1 mt-3 px-5 py-2.5 border rounded-lg hover:rounded-full " v-model="email" type="email" placeholder="Email Address">
                <input class="ml-56 mr-60 p-1 mt-3 px-5 py-2.5 border rounded-lg hover:rounded-full " v-model="password" type="password" placeholder="Password">
                <input class="ml-56 mr-60 p-1 mt-3 px-5 py-2.5 border rounded-lg hover:rounded-full " v-model="cpassword" type="text" placeholder="Confirm Password">


                <button @click.prevent="registerFrom" class="ml-56 mr-60 mt-4 bg-white text-black rounded-lg text-sm px-5 py-2.5 text-center font-medium hover:text-white hover:bg-black hover:rounded-full"> Register </button>
                
                <span class="text-white mb-5  ml-56">Have an account already?  
                <span class="font-extrabold text-blue-500 hover:text-white"> 
                <router-link to="/login" > Log in
                </router-link></span></span>

                <div class="text-red-500 mb-5 ml-56 " v-if="error">
                  <strong>{{ error }}......</strong>
                </div>

                <div class="text-red-500 mb-5 ml-56 " v-else-if="username_error || email_error">
                  <strong>{{ username_error }} .....</strong>
                </div>

                <!-- <div class="text-red-500 mb-5 ml-56 " v-else-if="email_error">
                  <strong>{{ email_error }}</strong>
                </div> -->
        </div>
    </div>

</template>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      first_name: null,
      username: null,
      email: null,
      password: null,
      cpassword: null,
      error: null,
      success: null,
      username_error: null,
      email_error:null
    }
  },
  methods: {
    registerFrom() {
        
      if (!this.first_name || !this.email || !this.username || !this.password || !this.cpassword) {
        this.error = 'Please add all fields'
      } else {
        const formData = {
          first_name: this.first_name,
          username: this.username,
          email: this.email,
          password: this.password,
          cpassword: this.cpassword
        }
        this.saveFormData(formData)
        // this.checkEmailUnique(formData);
      }
    },
    checkEmailUnique(formData) {
      axios.get(`http://127.0.0.1:8000/api/v1/check-email/?email=${formData.email}`)
        .then((response) => {
          const isUnique = response.data.is_unique
          if (isUnique) {
            this.registerFrom(formData)
          } else {
            this.error = 'Email is already taken'
          }
        })
        .catch(error =>{
            console.error(error);
        })
    },
    saveFormData(formData) {
        axios
          .post('http://127.0.0.1:8000/api/v1/users/', formData)         
          .then((response) => {
           
            if (response.data.email_error) {
           
              this.email_error = "Email or Username already exist";              
            } else if (response.data.username_error) {
            
              this.username_error = "Email or Username already exist";
              
            } else if (response.data.success) {
             
              this.success = response.data.success;
            }
            
          })
          .catch((error) => {
            console.error(error);
          });
        }

  }
}
</script>

