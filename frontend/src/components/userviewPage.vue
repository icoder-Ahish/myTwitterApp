<template>
    <div class="flex">    
    <leftsideBar/>

<!-- User card-->
<div class="ml-[100px]">
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
                    <div style="height:9rem; width:9rem;" class=" md rounded-full relative avatar">
                        <img style="height:9rem; width:9rem;" class="md rounded-full relative border-4 border-gray-900" src="../../public/userAvtar2.png" alt="">
                        <div class="absolute"></div>
                        
                    </div>
                </div>
            </div>
            <!-- Follow Button -->
            <div class="flex flex-col text-right">
                <button @click.prevent="follow"  v-if="isfollowing" class="flex justify-center  max-h-max whitespace-nowrap focus:outline-none  focus:ring   max-w-max border bg-transparent border-blue-500 text-blue-500  hover:border-blue-800  items-center hover:shadow-lg font-bold py-2 px-4 rounded-full mr-0 ml-auto">
                    Follow
                </button>
                <button @click.prevent="unfollow" v-else  class="flex justify-center  max-h-max whitespace-nowrap focus:outline-none  focus:ring   max-w-max border bg-transparent border-blue-500 text-blue-500  hover:border-blue-800  items-center hover:shadow-lg font-bold py-2 px-4 rounded-full mr-0 ml-auto">
                    Following
                </button>
                
            </div>
        </div>

        <!-- Profile info -->
        <div class="space-y-1 justify-center w-full mt-3 ml-3">
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
 <ul class="list-none ml-5 border mt-24 overflow-scroll h-[600px] ">
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

                <button @click="likeTweet(tweet.id)" v-if="!tweet.users_like.includes(userIdNumber)">
                      <i class="far fa-thumbs-up mr-3"></i>
                </button>
                <button @click="unlikeTweet(tweet.id)" v-else>
                      <i class="fas fa-thumbs-down mr-3"></i>
                </button>
               <p>{{ tweet.users_like.length  }}</p>

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
import leftsideBar from './leftsideBar.vue' ;
import axios from 'axios'

export default {
    components:{
        leftsideBar
    },
    computed: {
    follow_check() {
      return this.follow_data.is_followers;
    }
  },
  data() {    
    return {
      userId: null, viewUserId: '', username: '', userProfile: [],  user_data: [],
       isfollowing: true,
      tweetList: [],
      userIdNumber: null,
     }
    },
    created() {
    this.userId = localStorage.getItem('user_id')    
    this.viewUserId = this.$route.params.userId;
    this.username =  this.$route.params.username;
    this.userIdNumber = parseInt(this.userId)
 
    this.profileFetch(this.viewUserId)
    this.user_dataFetch(this.viewUserId)
    this.fetchTweets(this.viewUserId)
    this.filterFollow_user(this.userId, this.viewUserId)
  },
  methods:{
    likeTweet(tweetID) {
      const data = {
          "user_id" : this.userId       }
        axios.post(`http://localhost:8000/api/v2/tweet/${tweetID}/like/`,data)
        .then((response)=>{          
          this.fetchTweets(this.viewUserId);
        })        
    },
    unlikeTweet(tweetID) {
      const data = {
          "user_id" : this.userId
        }
        axios.post(`http://localhost:8000/api/v2/tweet/${tweetID}/unlike/`,data)
        .then((response)=>{         
          this.fetchTweets(this.viewUserId);
        })
    },
    filterFollow_user(userId, viewUserId) {
     const userId2 = userId;
     const viewId2 = viewUserId;
    axios.get('http://localhost:8000/api/v4/contacts/')
    .then((response) => {
        var followData = response.data;
    
        followData.forEach(entry => {
          
            if (entry.user_from == userId2 && entry.user_to == viewId2  && entry.is_followers == true) {
             
              this.isfollowing = false;
                
            }
        });
    });
},

    user_dataFetch(viewUserId){   
      axios.get(`http://localhost:8000/api/v1/users/${viewUserId}/`)
      .then((response)=>{
        this.user_data = response.data
      }).catch((error)=>{
        console.log("etching error", error)
      })
    },
    profileFetch(viewUserId){       
        axios.get(`http://localhost:8000/api/v4/profiles/${viewUserId}/`)
        .then((response)=>{
          this.userProfile = response.data
        })
    },  
    getFormattedDate(dateString) {
      const date = new Date(dateString);
      const month = date.toLocaleString("default", { month: "long" });
      const year = date.getFullYear();
      return `${month} ${year}`;
    },
    follow(){
      const timestamp = new Date().toISOString();
      const is_followers = true;
        axios.post('http://localhost:8000/api/v4/contacts/follow/',{
            "user_from": this.userId,
            "user_to": this.viewUserId,
            "is_followers": is_followers,
            "created": timestamp
        }).then((response)=>{
          this.follow_data= response.data;
        })
        this.isfollowing = false

        // this.fetchTweets(this.viewUserId)
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
   
    fetchTweets(viewUserId) {
      axios
        .get(`http://localhost:8000/api/v2/tweet/?author_id=${viewUserId}`)
        .then((response) => {
          this.tweetList = response.data.reverse()

        })
        .catch((error) => {
          console.error('Error fetching tweets:', error.response.data)
        })
    
  },
  unfollow(){
      const timestamp = new Date().toISOString();
      const is_followers = false;
        axios.post('http://localhost:8000/api/v4/contacts/unfollow/',{
            "user_from": this.userId,
            "user_to": this.viewUserId,
            "is_followers": is_followers,
            "created": timestamp
        }).then((response)=>{
          this.unfollow_data=response.data;
        })
        this.isfollowing = true

        // this.fetchTweets(this.viewUserId)
    },
  }

}

</script>

