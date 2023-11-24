<template>
  <!-- wrapup Container  -->
  <div class="leftsidebar flex mt-5">
    <!-- left side bar -->
    <leftsideBar @focus-input="focusInput"/>

    <!-- Middle bar -->
    <div
      class="middlebar ml-10 w-[600px] bg-white rounded-lg overflow-y-scroll over border-red-300 border-4 hover:border-red-700 "
      style="height: 680px;" >
      <!-- Tweet Section -->
      <div class=" ">
        <div class="px-5 py-3 border-b border-lighter flex items-center justify-between">
          <h1 class="text-xl font-bold">Home</h1>
          <i class="far fa-star text-xl text-blue" ></i>
        </div>
      </div>
      <div class="px-5 py-3 border-b-8 border-lighter flex">
        <div class="flex-none">
          <img
            src="../../public/userAvtar2.png"
            class="flex-none mt-2 w-12 h-12 rounded-full border border-lighter"
          />
        </div>
        <div class="ml-2">
          <form action="">
            <input
              type="text"
              v-model="body"
              placeholder="What's up?"
              class="mt-3 pl-1  pb-3 w-full border-black border-2 hover:bg-slate-400 hover:text-white focus:outline-none focus:bg-slate-400 focus:text-white "
              @keydown.enter.prevent="sendOnEnter"
              ref="inputField" 
              />
            <div class="flex items-center">
              
              <button
                type="button"
                @click.prevent="addTweet"
                class="bg-blue-950 hover:bg-blue-600 rounded-lg mt-2 px-5 hover:text-stone-100  text-white"
              >
                Post
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- tweet list -->
      <div class="flex flex-col-reverse">
        <div
          v-for="(tweet, index) in tweetList"
          :key="index"
          class="w-full p-4 border-b hover:bg-lighter flex"
        >
          <div class="flex-none mr-4">
            <img src="../../public/userAvtar2.png" class="h-12 w-12 rounded-full flex-none" />
          </div>
          <div class="w-full">
            <div class="flex items-center w-full">
              <p class="font-semibold">{{ username }}</p>
              <p class="text-sm text-dark ml-2">@{{ username }}</p>
              <p class="text-sm text-dark ml-2">{{ formatTimeAgo(tweet.created) }}</p>
              <i class="fas fa-angle-down text-dark ml-auto"></i>
            </div>
            <a href=""></a>
            <p class="py-2 p-4 bg-gray-600 text-white mt-2">
              {{ tweet.body }}
            </p>
            <p class="py-2">
              {{ tweet.retweet }}
            </p>
            <div class="flex items-center justify-between w-full">
              <div class="flex items-center text-sm text-dark">
                <button @click.prevent="addComments(tweet.id)"><i class="far fa-comment mr-3"></i></button>
                <!-- <p>1</p> -->
              </div>

              <div class="flex items-center text-sm text-dark">
                <button href="" @click="toggleModal(tweet.id)"><i class="fas fa-retweet mr-3"></i></button>
                <p>0</p>
                <div class="lg:w-full relative">
                <div v-if="dropdown === true"
                  class="absolute bottom-0 left-0 w-64 rounded-lg shadow-md border-lightest bg-white mb-16">
                  <button @click="dropdown = false"
                    class="flex items-center w-full hover:bg-lightest p-2 focus:outline-none">
                    <button>repost</button>
                    <button>Quote</button>
                 
                  </button> 
                </div> 
    </div>
              </div>

              <div class="flex items-center text-sm text-dark">
          
                <button @click="likeTweet(tweet.id)" v-if="!tweet.users_like.includes(userIdNumber)">
                      <i class="far fa-thumbs-up mr-3"></i>
                </button>
                <button @click="unlikeTweet(tweet.id)" v-else>
                      <i class="fas fa-thumbs-down mr-3"></i>
                </button>
                
               <p>{{ tweet.users_like.length  }}</p>
              </div>
            
              <div class="flex items-center  text-dark">
                <button @click.prevent="deleteTweet(tweet.id)"> <i class="fa fa-trash mr-3"></i> </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="retweetList.length>0" class="dividar bg-slate-500 h-6 flex  justify-center">
        <p class="">  Your Retweets </p>
      </div>
      <!-- Retweet list -->
      <div class="flex flex-col-reverse">
        <div
          v-for="(retweet, index) in retweetList"
          :key="index"
          class="w-full p-4 border-b hover:bg-lighter flex"
        >
          <div class="flex-none mr-4">
            <img src="../../public/userAvtar2.png" class="h-12 w-12 rounded-full flex-none" />
          </div>
          <div class="w-full">
            <div class="flex items-center w-full">
              <p class="font-semibold">{{ username }}</p>
              <p class="text-sm text-dark ml-2">@{{ username }}</p>
              <p class="text-sm text-dark ml-2">{{ formatTimeAgo(retweet.created) }}</p>
              <i class="fas fa-angle-down text-dark ml-auto"></i>
            </div>
            <a href=""></a>
           
            <p class="py-2 p-4 bg-gray-600 text-white mt-2">
              {{ retweet.retweet }}
            </p>
            <div class="flex items-center justify-between w-full">
          

              <div class="flex items-center text-sm text-dark">
          
                <button @click="likeRetweet(retweet.id)" v-if="!retweet.users_like.includes(userIdNumber)">
                      <i class="far fa-thumbs-up mr-3"></i>
                </button>
                <button @click="unlikeRetweet(retweet.id)" v-else>
                      <i class="fas fa-thumbs-down mr-3"></i>
                </button>
                
               <p>{{ retweet.users_like.length  }}</p>
              </div>
            
              <div class="flex items-center  text-dark">
                <button @click.prevent="deleteRetweet(retweet.id)"> <i class="fa fa-trash mr-3"></i> </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- <div
        v-for="(follow, index) in following"
        :key="index"
        class="w-full p-4 border-b hover:bg-lighter flex"
      >
        <div class="flex-none mr-4">
          <img :src="`${follow.src}`" class="h-12 w-12 rounded-full flex-none" />
        </div>
        <div class="w-full">
          <div class="flex items-center w-full">
            <p class="font-semibold">{{ follow.name }}</p>
            <p class="text-sm text-dark ml-2">{{ follow.handle }}</p>
            <p class="text-sm text-dark ml-2">{{ follow.time }}</p>
            <i class="fas fa-angle-down text-dark ml-auto"></i>
          </div>
          <p class="py-2">
            {{ follow.tweet }}
          </p>
          <div class="flex items-center justify-between w-full">
            <div class="flex items-center text-sm text-dark">
              <i class="far fa-comment mr-3"></i>
              <p>{{ follow.comments }}</p>
            </div>
            <div class="flex items-center text-sm text-dark">
              <i class="fas fa-retweet mr-3"></i>
              <p>{{ follow.retweets }}</p>
            </div>
            <div class="flex items-center text-sm text-dark">
              <i class="fas fa-heart mr-3"></i>
              <p>{{ follow.like }}</p>
            </div>
            <div class="flex items-center text-sm text-dark">
              <i class="fas fa-share-square mr-3"></i>
            </div>
          </div>
        </div>
      </div> -->

    </div>

    <!-- right side bar -->
    <div style="height: 680px;"
      class="flex-shrink rounded-lg w-[400px] ml-10 bg-white overflow-y-scroll border-red-300 border-4 hover:border-red-700"
    >
      
     
      <div class="w-full rounded-lg bg-lightest my-4">
        <div class="p-3">
          <p class="text-lg font-bold">Who to Follow</p>
        </div>

        <!-- Follow User Display -->
            <div>
                  <div v-for="user in follow" :key="user.id" class="w-full flex hover:bg-lighter p-3 border-t border-lighter">
                    <img :src="`/public/anonymous-avtar.jpeg`" class="w-12 h-12 rounded-full border border-lighter" />
                    <div class="hidden lg:block ml-4">
                      <p class="text-sm font-bold leading-tight">{{ user.username }}</p>
                      <p class="text-sm leading-tight">{{ user.username }}</p>
                    </div>
                    <button
                      @click="viewUser(user.id, user.username)"
                      class="ml-auto text-sm text-white py-1 px-4 rounded-full border-2 border-blue bg-blue-950 hover:bg-blue-600"
                    >
                      View
                    </button>
                  </div>
              </div>
      </div>
    </div>
  </div>

  <!-- my model -->
  <div id="modal" v-show="isModalVisible"  tabindex="-1" class="fixed top-0 left-0 right-0 bottom-0 
  z-50 flex  justify-center  p-4 overflow-x-hidden overflow-y-auto md:inset-0">
    <div class="relative w-[700px] ">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <button @click="toggleModal" type="button" class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="popup-modal">
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                </svg>
                <span class="sr-only">Close modal</span>
            </button>
            <div class="p-6 ">
                <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400"> Repost</h3>
                <div class="mb-6">
                  <div class="py-2 px-4 mb-4 bg-white rounded-lg rounded-t-lg border border-gray-200 dark:bg-gray-800 dark:border-gray-700">
                      <label for="comment" class="sr-only">Write Your comment....</label>
                      <textarea id="comment" rows="6" v-model="retweet_content"
                          class="px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 focus:outline-none dark:text-white dark:placeholder-gray-400 dark:bg-gray-800"
                          placeholder="Write a comment..." required></textarea>
                  </div>
                
              </div>
              <article v-if="specificTweet" class="p-6 mb-6 ml-10 text-base bg-white rounded-lg dark:bg-gray-600" >
                  <footer class="flex justify-between items-left mb-2">
                      <div class="flex items-center">
                          <p class="inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white"><img
                                  class="mr-2 w-6 h-6 rounded-full"
                                  src="../../public/download1.jpeg"
                                  alt="">{{username}}</p>
                          <p class="text-sm text-gray-600 dark:text-gray-400"><time pubdate datetime="2022-02-08"
                                  title="February 8th, 2022">{{ formatTimeAgo(specificTweet.created) }}</time></p>
                      </div>            
                  </footer>
                  
                  <p class="text-gray-500 dark:text-gray-400">{{specificTweet.body}}</p>
              </article>

              <button type="submit"  @click.prevent="retweet(specificTweet.id)"
                      class=" py-2.5 px-4 text-xs font-medium text-center text-blsck bg-white rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                      Post
              </button>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import leftsideBar from '@/components/leftsideBar.vue'
// import {useUserStore} from '@/stores/user.js'
// import {useuserTokenStore} from '@/stores/userToken.js'

export default {
  // setup() {
  //       const userTokenStore = useuserTokenStore()
  //       const user_token = userTokenStore.user_tokeen
  //       return {
  //         user_token
  //   }
  // },
  components: {
    leftsideBar
  },
  data() {
    return {
      dropdown: false,
      isModalVisible: false,
      username: '',
      userId: null,
     
      retweet_id: null,
      body: '',
      trending: [
       
      ],
      follow: [],
      // following: [
      //   {src: 'https://randomuser.me/api/portraits/women/52.jpg', name: 'Giza Lamo', handle: '@giza', time: '1.2 hr', tweet: 'The very essence of TailWindCSS??', comments: '500', retweets: '250', like: '52,003'},
      //   {src: 'https://randomuser.me/api/portraits/women/62.jpg', name: 'Doug mama', handle: '@mama', time: '25 min', tweet: 'Should I use Flutter now?', comments: '1000', retweets: '500', like: '70,003'},
      //   {src: 'https://randomuser.me/api/portraits/men/63.jpg', name: 'Ezy Pzy', handle: '@ezypzy', time: '2.7 hr', tweet: 'Get Ready for the tech revolution', comments: '10,000', retweets: '100,002', like: '200,003'},
      // ],
      tweetList: [],
      retweetList: [],
      userIdNumber: null,
      retweet_content: [],
    }
  },
  created() {
    this.username = sessionStorage.getItem('username')
    this.userId = sessionStorage.getItem('user_id')
    this.userIdNumber = parseInt(this.userId)
    this.fetchTweets();
    this.fetchRetweets();
    this.fetchUsers();
  },
 
   computed: {
    specificTweet() {
      // Find the tweet with id: 5 in the tweetList
      return this.tweetList.find((tweet) => tweet.id === this.retweet_id);
    },
  },

  methods: {  
    toggleModal(retweetId) {
            this.isModalVisible = !this.isModalVisible;

            this.retweet_id = retweetId
    },
   
    focusInput() {
      this.$refs.inputField.focus(); // Set focus on the input field
    },
    likeTweet(tweetID) {
      const data = {
          "user_id" : this.userId       }
        axios.post(`http://localhost:8000/api/v2/tweet/${tweetID}/like/`,data)
        .then((response)=>{          
          this.fetchTweets();
        })        
    },
    unlikeTweet(tweetID) {
      const data = {
          "user_id" : this.userId
        }
        axios.post(`http://localhost:8000/api/v2/tweet/${tweetID}/unlike/`,data)
        .then((response)=>{         
          this.fetchTweets();
        })
    },
  
    async addTweet() {
      const userId = sessionStorage.getItem('user_id')
      const tweetContent = this.body
      axios
        .post('http://localhost:8000/api/v2/tweet/', {
          author: userId,
          content: tweetContent
        })
        .then((response) => {
          this.body = '';
          if(response.data.error)
          {
            alert(response.data.error)
          }else{
            this.fetchTweets();
          };
         
        })
        .catch((error) => {
          console.log('Error creating tweet:', error.response.data)
        })
    },
    fetchTweets() {
      const  userId = sessionStorage.getItem('user_id');
      // console.log(userId);
      axios
        .get(`http://localhost:8000/api/v2/tweet/?author_id=${userId}`)
        .then((response) => {
          this.tweetList = response.data.reverse()
         
        })
        .catch((error) => {
          console.error('Error fetching tweets:', error.response.data)

          // alert("Your tweet contain bad words, Pease use apporoprit language");
        })
    },
    retweet(specificTweet_id){
      console.log(specificTweet_id);
      const retweet_body = this.retweet_content;
      console.log(retweet_body);
      const data ={
        "author": this.userId,
        "tweet": specificTweet_id,
        "retweet": retweet_body
      }
      axios.post('http://localhost:8000/api/v2/retweet/',data)
      .then((response)=>{
        this.retweet_content = '';
        // this.retweetList = response.data
        
        this.isModalVisible = !this.isModalVisible;
        this.fetchRetweets();
      })
    },
    fetchRetweets() {
      const  userId = sessionStorage.getItem('user_id');
      axios
        .get(`http://localhost:8000/api/v2/retweet/?author_id=${userId}`)
        .then((response) => {
       
          this.retweetList = response.data.reverse();
       })
        .catch((error) => {
          console.error('Error fetching tweets:', error.response.data)
        })
    },
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
    fetchUsers(){
      axios
        .get('http://localhost:8000/api/v1/users/') 
        .then((response) => {
          const sortedUsers = response.data.sort((a, b) => b.followers_count - a.followers_count);
        const filteredUsers = sortedUsers.filter((user) => user.username !== this.username);
        // console.log(filteredUsers)
        this.follow = filteredUsers.slice(0, 3);       
        })
        .catch((error) => {
          console.error('Error fetching users:', error.response.data);
        });
    },
    deleteTweet(tweetid){
      axios.delete(`http://localhost:8000/api/v2/tweet/${tweetid}/`)
        .then(()=>{
        
          this.fetchTweets()
        })
        .catch((error) => {
          console.error('Error fetching tweets:', error.response.data)
        })
     },
     likeRetweet(retweetID) {
      
      const data = {
          "user_id" : this.userId       }
        axios.post(`http://localhost:8000/api/v2/retweet/${retweetID}/like/`,data)
        .then((response)=>{   
              
          this.fetchRetweets();
        })        
    },
    unlikeRetweet(retweetID) {
    
      const data = {
          "user_id" : this.userId
        }
        axios.post(`http://localhost:8000/api/v2/retweet/${retweetID}/unlike/`,data)
        .then((response)=>{         
          this.fetchRetweets();
        })
    },
    deleteRetweet(retweetid){
      axios.delete(`http://localhost:8000/api/v2/retweet/${retweetid}/`)
        .then(()=>{
        
          this.fetchRetweets()
        })
        .catch((error) => {
          console.error('Error fetching tweets:', error.response.data)
        })
     },
    
     viewUser(userId, username){
        this.$router.push({
          name: 'userview',
          params:{
            userId,
            username
          }
        })
     },
     addComments(tweetId){
        this.$router.push({
          name: 'comments',
          params:{
            tweetId,
            
          }
        })
     },

     sendOnEnter() {     
        this.addTweet();     
    }
  }
}


</script>

<style></style>