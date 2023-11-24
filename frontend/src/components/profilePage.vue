<template>
    <div class="flex">    
    <leftsideBar/>

<!-- User card-->
<div class="ml-[100px] border-2  mt-5 bg-gray-800 p-2">
    <div class="mx-2">
            <h2 class="mb-0 text-xl font-bold text-white"><span> {{user_data.username}} </span></h2>
            <!-- <p class="mb-0 w-48 text-xs text-gray-400">0 Tweets_count</p> -->
        </div>
    <div class="w-full mt-16 bg-cover bg-no-repeat bg-center" style="height: 200px; background-image: url(../../public/bgavtar.jpeg);">
        <!-- <img class="opacity-0 w-full h-full" src="../../public/facebooklogo.png" alt=""> -->
    </div>
    <div class="p-4">
        <div class="relative flex w-full">
            <!-- Avatar -->
            <div class="flex flex-1">
                <div style="margin-top: -6rem;">
                    <div style="height:9rem; width:9rem;" class="md rounded-full relative avatar">
                        <img style="height:9rem; width:9rem;" class="md rounded-full relative border-4 border-gray-900" src="../../public/userAvtar2.png" alt="">
                        <div class="absolute"></div>
                    </div>
                </div>
            </div>
            <!-- Follow Button -->
            <div class="flex flex-col text-right">
                <button @click.prevent="profileEdit(userId)"  class="flex justify-center  max-h-max whitespace-nowrap focus:outline-none  focus:ring   max-w-max border bg-transparent border-blue-500 text-blue-500  hover:border-blue-800  items-center hover:shadow-lg font-bold py-2 px-4 rounded-full mr-0 ml-auto">
                    Add Bio
                </button>
            </div>
        </div>

        <!-- Profile info -->
        <div class="space-y-1 justify-center  w-[600px] mt-3 ml-3">
            <!-- User basic-->
            <div>
                <h2 class="text-xl leading-6 font-bold text-white">{{user_data.username}} </h2>
                <p class="text-sm leading-5 font-medium text-gray-600">@{{user_data.username}} </p>
            </div>
            <!-- Description and others -->
            <div class="mt-3">
                <p class="text-white leading-tight mb-2">{{ userProfile.bio }} </p>
                <div class="text-gray-600 flex">
                    <!-- <span><a href="" target="#" class="leading-5 ml-1 text-blue-400">www.myProfile.com</a></span> -->
                     <span class="leading-5 ml-1">Joined {{getFormattedDate(user_data.date_joined) ?? 0}}</span>
                </div>
            </div>
            <div class="pt-3 flex justify-start items-start w-full divide-x divide-gray-800 divide-solid">
                <div class="text-center pr-3" ><span class="font-bold text-white">{{ userProfile.following_count ?? 0 }}</span><span class="text-gray-600"> Following</span></div>
                <div class="text-center px-3"><span class="font-bold text-white">{{ userProfile.followers_count ?? 0}} </span><span class="text-gray-600"> Followers</span></div>
            </div>
        </div>
    </div>
    <hr class="border-gray-800">
 </div>
 <!-- tweet list -->
 <div v-if="tweetList.length > 0">
 <ul class="list-none ml-5 border m-5 overflow-scroll h-[650px] w-[400px]">
   <li v-for="(tweet,index) in tweetList" :key="index">                  
    <div class="flex flex-col-reverse">
        <div class="w-full p-4 border-b hover:bg-lighter flex" >
          <div class="flex-none mr-4">
            <img src="../../public/userAvtar2.png" class="h-12 w-12 rounded-full flex-none" />
          </div>
          <div class="w-full">
            <div class="flex items-center w-full">
              <p class="font-semibold text-white" >{{ username }}</p>
              <p class="text-sm  text-white ml-2">@{{ username }}</p>
              <p class="text-sm text-white ml-2">{{formatTimeAgo(tweet.created)}}</p>
              
            </div>
            <p class="py-2 text-white">
              {{ tweet.body }}
            </p>
            <div class="flex items-center justify-between w-full">
              <div class="flex items-center text-sm text-white">
                <button href=""><i class=" far fa-comment mr-3"></i></button>
                <p>1</p>
              </div>
              <div class="flex items-center text-sm text-white">
                <button href=""><i class="fas fa-retweet mr-3"></i></button>
                <p>0</p>
              </div>
              <div class="flex items-center text-sm text-white">
                <button href=""><i class="fas fa-heart mr-3"></i></button>
                <p>2</p>
              </div>
              <div class="flex items-center text-white">
                <button  @click.prevent="deleteTweet(tweet.id)"> <i class="fa fa-trash mr-3"></i> </button>
              </div>
            </div>
          </div>
        </div>
      </div>
   </li>
 </ul>
</div>
</div>
</template>

<script >

import leftsideBar from './leftsideBar.vue';
import axios from 'axios'

export default {
    components:{
        leftsideBar
    },
    data() {
    return {
      username: '', userId:'', userProfile: [], user_data: [],  bio_option: true,
      tweetList: [],
     }
    },
    created() {
    this.username = sessionStorage.getItem('username');
    this.userId = sessionStorage.getItem('user_id');
    this.profileFetch(this.userId)
    this.user_dataFetch(this.userId)
    this.fetchTweets(this.userId)
  },
  methods:{
    user_dataFetch(userId){
      axios.get(`http://localhost:8000/api/v1/users/${userId}/`)
      .then((response)=>{
        this.user_data = response.data
      }).catch((error)=>{
        console.log("etching error", error)
      })
    },
    profileFetch(userId){
        axios.get(`http://localhost:8000/api/v4/profiles/${userId}/`)
        .then((response)=>{
          this.userProfile = response.data
        
        })
    },
    profileEdit(userId){
        const bio = window.prompt('Please enter your bio. You can add ths only once!!')
        axios.post('http://localhost:8000/api/v4/profiles/',{        
          "user" : userId,
		      "bio": bio
        })
        .then((response)=>{
          this.userProfile = response.data

          this.bio_option = false
        })
    },
    getFormattedDate(dateString) {
      const date = new Date(dateString);
      const month = date.toLocaleString("default", { month: "long" });
      const year = date.getFullYear();
      return `${month} ${year}`;
    },
        // Time format method
    formatTimeAgo(createdAt) {
      const createdTime = new Date(createdAt)
      const currentTime = new Date()
      const timeDifferenceInSeconds = Math.floor((currentTime - createdTime) / 1000)

      if (timeDifferenceInSeconds < 60) {
        return `${timeDifferenceInSeconds} sec ago`
      } else if (timeDifferenceInSeconds < 3600) {
        const minutes = Math.floor(timeDifferenceInSeconds / 60)
        return `${minutes} min ago`
      } else if (timeDifferenceInSeconds < 86400) {
        const hours = Math.floor(timeDifferenceInSeconds / 3600)
        return `${hours} hour ago`
      } else {
        const days = Math.floor(timeDifferenceInSeconds / 86400)
        return `${days} days ago`
      }
    },
   
    fetchTweets(userId) {    
      axios
        .get(`http://localhost:8000/api/v2/tweet/?author_id=${userId}`)
        .then((response) => {
          this.tweetList = response.data.reverse()         
        })
        .catch((error) => {
          console.error('Error fetching tweets:', error.response.data)
        })
    
  },
  }

}

</script>

