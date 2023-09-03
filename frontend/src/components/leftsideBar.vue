<template>
    <!-- left side bar -->
    <div class=" bg-white w-72 rounded-lg border-lighter  border-red-300 border-4 hover:border-red-700 flex-shrink-0 sticky ">
                
        
                <button class="h-12 w-12  text-3xl rounded-full text-blue">
                    <i class="fab fa-twitter"></i>
                </button>

                <div>
                    <router-link to="/home"  class="hover:bg-slate-500 hover:text-blue flex items-center py-2 px-4 hover:bg-lightblue rounded-full mr-auto mb-3 }">
                        <i class="fas fa-home text-2xl mr-4 text-left"></i>
                        <p class="text-lg font-semibold text-left hidden lg:block"> Home </p>
                    </router-link>

                    <!-- <button  class="hover:bg-slate-500 hover:text-blue flex items-center py-2 px-4 hover:bg-lightblue rounded-full mr-auto mb-3 }">
                        <i class="fas fa-hashtag text-2xl mr-4 text-left"></i>
                        <p class="text-lg font-semibold text-left hidden lg:block"> Explore </p>
                    </button> -->

                    <button  class="hover:bg-slate-500 hover:text-blue flex items-center py-2 px-4 hover:bg-lightblue rounded-full mr-auto mb-3 }">
                        <i class="far fa-bell text-2xl mr-4 text-left"></i>
                        <p class="text-lg font-semibold text-left hidden lg:block"> Notifications </p>
                    </button>

                    <router-link to="/message"  class="hover:bg-slate-500 hover:text-blue flex items-center py-2 px-4 hover:bg-lightblue rounded-full mr-auto mb-3 }">
                        <i class="far fa-envelope text-2xl mr-4 text-left"></i>
                        <p class="text-lg font-semibold text-left hidden lg:block"> Messages </p>
                    </router-link>

                    <router-link to="/profile"  class="hover:bg-slate-500 hover:text-blue flex items-center py-2 px-4 hover:bg-lightblue rounded-full mr-auto mb-3 }">
                        <i class="far fa-user text-2xl mr-4 text-left"></i>
                        <p class="text-lg font-semibold text-left hidden lg:block"> Profile </p>
                    </router-link>
                </div>


                <button @click="emitFocusEvent" class="text-white mb-6 bg-blue-950 rounded-full font-semibold focus:outline-none w-12 h-12 lg:h-auto lg:w-full p-3 hover:bg-blue-600">
                <p class="hidden lg:block">Tweet</p>
                <i class="fas fa-plus lg:hidden"></i>
                
               </button>

                <hr>
                <!-- Dropdown -->
                <div class="lg:w-full relative">
                    <button @click="dropdown = !dropdown" class="flex items-center w-full hover:bg-lightblue rounded-full p-2 focus:outline-none">
                        <img src="../../public/userAvtar2.png" class="w-10 h-10 rounded-full border border-lighter" />
                        <div class="hidden lg:block ml-4">
                        <p class="text-sm font-bold leading-tight"> {{ username }} </p>
                        <p class="text-sm leading-tight"> @{{ username }} </p>
                        </div>
                        <i class="hidden lg:block fas fa-angle-down ml-auto text-lg"></i>
                    </button>
                    <div v-if="dropdown === true" class="absolute bottom-0 left-0 w-64 rounded-lg shadow-md border-lightest bg-white mb-16">
                        <button @click="dropdown = false" class="flex items-center w-full hover:bg-lightest p-2 focus:outline-none">
                        <img src="../../public/userAvtar2.png" class="w-10 h-10 rounded-full border border-lighter" />
                        <div class="ml-4">
                            <p class="text-sm font-bold leading-tight"> {{ username }} </p>
                            <p class="text-sm leading-tight"> @{{ username }}  </p>
                        </div>
                        <i class="fas fa-check ml-auto test-blue"></i>
                        </button>
                        <!-- <button @click="dropdown = false" class="w-full text-left hover:bg-lightest border-t border-lighter p-3 test-sm focus:outline-none">
                        Add an existing account
                        </button> -->
                        <button @click.prevent="logOut" class="w-full text-left hover:bg-lightest border-t border-lighter p-3 test-sm focus:outline-none">
                        Log out @{{username}}
                        </button>
                    </div>
                </div>
        </div >
</template>

<script>

export default {
  
  data() {
    return {
    username: '',
    dropdown: false,  
    }
 },
 created(){
    this.username = localStorage.getItem('username');
},
methods:{
    emitFocusEvent() {
      this.$emit('focus-input'); // Emit custom event to parent component
    },
    logOut(){
        localStorage.removeItem('user_id')
        localStorage.removeItem('username')
        localStorage.removeItem('token')

        window.location.reload()
    }
}

}
</script>
