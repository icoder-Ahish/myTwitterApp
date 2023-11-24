<template>

<section class="bg-white dark:bg-gray-900 py-8 lg:py-16">
    
  <div class="max-w-2xl mx-auto px-4">
      <div class="flex justify-between items-center mb-6">
        <!-- <p class="text-white"></p> -->
        <h2 class="text-lg lg:text-2xl font-bold text-gray-900 dark:text-white">Discussion ({{comments_data.length}})</h2>
    </div>
<!--   
<div id="alert-1" class="flex items-center p-4 mb-4 text-blue-800 rounded-lg bg-blue-50 dark:bg-gray-800 dark:text-blue-400" role="alert">
  <svg class="flex-shrink-0 w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
  </svg>
  <span class="sr-only">Info</span>
  <div class="ml-3 text-sm font-medium">
    A simple info alert with an <a href="#" class="font-semibold underline hover:no-underline">example link</a>. Give it a click if you like.
  </div>
    <button onClick="hideAlert" type="button" class="ml-auto -mx-1.5 -my-1.5 bg-blue-50 text-blue-500 rounded-lg focus:ring-2 focus:ring-blue-400 p-1.5 hover:bg-blue-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-blue-400 dark:hover:bg-gray-700" data-dismiss-target="#alert-1" aria-label="Close">
      <span class="sr-only">Close</span>
      <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
      </svg>
  </button>
</div> -->

    <form class="mb-6">
        <div class="py-2 px-4 mb-4 bg-white rounded-lg rounded-t-lg border border-gray-200 dark:bg-gray-800 dark:border-gray-700">
            <label for="comment" class="sr-only">Your comment</label>
            <textarea id="comment" rows="6" v-model="comment"
                class="px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 focus:outline-none dark:text-white dark:placeholder-gray-400 dark:bg-gray-800"
                placeholder="Write a comment..." required></textarea>
        </div>
        <button type="submit"  @click.prevent="addComments"
            class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-blsck bg-white rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
            Post comment
        </button>
    </form>
    
    <ul>
        <li v-for="(comment, index) in comments_data " :key="index" >
        <article class="p-6 mb-6 text-base bg-white rounded-lg dark:bg-gray-800" >
        <footer class="flex justify-between items-center mb-2">
            <div class="flex items-center">
                <p class="inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white"><img
                        class="mr-2 w-6 h-6 rounded-full"
                        src="../../public/download1.jpeg"
                        alt="Michael Gough">{{ comment.author_name }}</p>
                <p class="text-sm text-gray-600 dark:text-gray-400"><time pubdate datetime="2022-02-08"
                        title="February 8th, 2022">{{ formatTimeAgo(comment.created) }}</time></p>
            </div>            
        </footer>
        <p class="text-gray-500 dark:text-gray-400">{{ comment.content }}.</p>
    </article>
 
        </li>
    </ul>
    

   

  </div>
</section>
</template>

<script >

import axios from 'axios';
export default {
    data(){
        return{
            tweetId : '',
            comment: '',
            userId: '',
            comments_data: [],
            error:''
        }
    },
    created(){
        this.tweetId = this.$route.params.tweetId;
        this.userId = sessionStorage.getItem('user_id')
        this.fetchComments()
    },
    methods:{     
        addComments(){  
            if (!this.comment  ) {
        this.error = 'Please add all fields'
        console.log('Please fill the  fields');
      }else{
        const comment = this.comment;
            const tweetID = this.tweetId
            const data = {
                "tweet_id": tweetID,
                "author_id": this.userId,
                "content": comment
            }
            axios.post('http://localhost:8000/api/v2/comment/', data)
            .then((response)=>{      
                   
                this.fetchComments(this.viewUserId);
                this.comment = '';
            }) 
      }    
     
    },
    fetchComments(){
        const tweetID = this.tweetId
        axios.get(`http://localhost:8000/api/v2/comments/tweet/${tweetID}/`)
        .then((response)=>{
            this.comments_data = response.data.reverse();
        })
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
}
}

</script>
