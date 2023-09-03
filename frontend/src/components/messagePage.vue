<template>
    <!-- Chat room -->
    <div class="flex h-screen antialiased text-gray-800">
    <div class="flex flex-row h-full w-full overflow-x-hidden">
      <div class="flex flex-col py-8 pl-6 pr-2 w-64 bg-white flex-shrink-0">
        <router-link to="/home"  class="hover:bg-slate-500 ml-3 hover:text-blue flex items-center py-2 px-4 hover:bg-lightblue rounded-full mr-auto mb-3 }">
                        <i class="fas fa-home text-2xl mr-4 text-left"></i>
                        <p class="text-lg font-semibold text-left hidden lg:block"> Home </p>
        </router-link>
        <div class="flex flex-row items-center justify-center h-12 w-full">
          <div class="flex items-center justify-center rounded-2xl text-indigo-700 bg-indigo-100 h-10 w-10">
            <!-- <button class="h-12 w-12 hover:bg-lightblue text-3xl rounded-full text-blue">
                    <i class="fab fa-twitter"></i>
           </button> -->
            <svg class="w-6 h-6"   fill="none" stroke="currentColor"  viewBox="0 0 24 24"  xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"  d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"              ></path>
            </svg>
          </div>
          <div class="ml-2 font-bold text-2xl">Chat Room</div>
        </div>
        <div class="flex flex-col items-center bg-indigo-100 border border-gray-200 mt-4 w-full py-6 px-4 rounded-lg">
          <div class="h-20 w-20 rounded-full border overflow-hidden">
            <img src="../../public/userAvtar2.png" alt="Avatar"  class="h-full w-full" />
          </div>
          <div class="text-sm font-semibold mt-2">{{ username }}.</div>
    
          <div class="flex flex-row items-center mt-3">
            <!-- <div
              class="flex flex-col justify-center h-4 w-8 bg-indigo-500 rounded-full"
            >
              <div class="h-3 w-3 bg-white rounded-full self-end mr-1"></div>
            </div> -->
            <!-- <div class="leading-none ml-1 text-xs">Active</div> -->
          </div>
        </div>
        <div class="flex flex-col mt-8">
          <div class="flex flex-row items-center justify-between text-xs">
            <span class="font-bold">Active Users</span>
            <span
              class="flex items-center justify-center bg-gray-300 h-4 w-4 rounded-full"
              >{{ filteredUsers.length }}</span
            >
          </div>
          <div class="flex flex-col space-y-1 mt-4 -mx-2 h-48 overflow-y-auto">
              <button v-for="(user, index) in filteredUsers" :key="index" @click="selectReceiver(user.id, user.username)" class="flex flex-row items-center hover:bg-gray-100 rounded-xl p-2">
                <div class="flex items-center justify-center h-8 w-8 bg-indigo-200 rounded-full">
                  {{ user.username.charAt(0).toUpperCase() }}
                </div>
                <div class="ml-2 text-sm font-semibold">{{ user.username }}</div>
              </button>
          </div>

    <!-- Footer --> <hr>
          <div class="flex flex-col space-y-1 mt-4 -mx-2">
            <button
              class="flex flex-row items-center hover:bg-gray-100 rounded-xl p-2"
            >
              <div
                class="flex items-center justify-center h-8 w-8 bg-indigo-200 rounded-full"
              >M
              <!-- {{ getFirstLetter(user.username) }} -->
              </div>
              <div class="ml-2 text-sm font-semibold">{{username}}</div>
            </button>
          </div>
        </div>
      </div>


       <div class="flex flex-col flex-auto h-full p-6">
        <div class="flex flex-col flex-auto flex-shrink-0 rounded-2xl bg-gray-100 h-full p-4" >
          <div class="flex flex-col h-full overflow-x-auto mb-4">
            <div class="flex flex-col h-full">

              <!-- Conversations -->
              <div class="grid grid-cols-12 gap-y-2" v-for="message in messages" :key="message.id">
             
              
                  <!-- Sender side -->
                <div class="col-start-6 col-end-13 p-3 rounded-lg" v-if="message.sender.username === username ">
                  <div class="flex flex-col ">                                  
                    <div  class="mt-3  flex relative ml-3 text-sm bg-white py-2 px-4 shadow rounded-xl flex-row" >
                        
                      <div class="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-500 flex-shrink-0"   >
                      {{getFirstLetter(username)}}
                    </div> 
                        <div class="mt-2 ml-2">
                            
                            {{ message.content }}
                            <span class="text-xs text-gray-500">{{ formatDate(message.timestamp) }}</span>
                         </div>                    
                    </div>
                  </div>
                </div>

                  <!-- Reciver side messages -->
                  <div class="col-start-1 col-end-8 p-3 rounded-lg" v-else>
                    
                  <div class="flex flex-col ">                                   
                    <div  class="mt-3 flex flex-row relative ml-3 text-sm bg-white py-2 px-4 shadow rounded-xl " >
                      
                          <div class="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-500 flex-shrink-0"   >
                            {{getFirstLetter(recevier_name)}}
                          </div> 
                        <div class="mt-2 ml-2">
                            
                            {{ message.content }}
                            <span class="text-xs text-gray-500">{{ formatDate(message.timestamp) }}</span>
                         </div>                    
                    </div>
                  </div>
                </div>


              </div>
            </div>
          </div>
          <div class="flex flex-row items-center h-16 rounded-xl bg-white w-full px-4"   >
            <div>
              <button class="flex items-center justify-center text-gray-400 hover:text-gray-600" >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" >
                  <path  stroke-linecap="round"  stroke-linejoin="round"   stroke-width="2"   d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" ></path>
                </svg>
              </button>
            </div>
            <div class="flex-grow ml-4">
              <div class="relative w-full">
                <input  type="text" class="flex w-full border rounded-xl focus:outline-none focus:border-indigo-300 pl-4 h-10" v-model="content" />
                <button  class="absolute flex items-center justify-center h-full w-12 right-0 top-0 text-gray-400 hover:text-gray-600"    >
                  <svg
                    class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"   xmlns="http://www.w3.org/2000/svg" >
                    <path
                      stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" ></path>
                  </svg>
                </button>
              </div>
            </div>
            <div class="ml-4">
              <button class="flex items-center justify-center bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white px-4 py-1 flex-shrink-0" @click.prevent="sendMessage" >
                <span>Send</span>
                <span class="ml-2">
                  <svg
                    class="w-4 h-4 transform rotate-45 -mt-px" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"                 >
                    <path
                      stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
                  </svg>
                </span>
              </button>
            </div>
          </div>
        </div>
      </div> 
    </div>
  </div>

   
</template>

<script>
import axios from 'axios';


export default {

  data() {
    return {
      username: '',
      userId: '',
      dropdown: false,
      filteredUsers: [],
      firstLetter: '',
      recevier_name:'',
      recevier_id:'',
      content:'',
      recevier_isSelected: false,

      messages: '',

      // senderMessages: [],
      // receiverMessages: [],

       // Set this to the receiver's name
      senderName: "",   
    };
  },
  created() {
    this.username = localStorage.getItem('username');
    this.userId = localStorage.getItem('user_id');
    this.fetchUsers();
    this.firstLetter = this.getFirstLetter(this.username);
  },

  mounted() {
    window.addEventListener('keydown', this.sendEnter);
  },

  beforeUnmount() {
    window.removeEventListener('keydown', this.sendEnter);
  },
  methods: {
    formatDate(timestamp) {
    // Format the timestamp into a human-readable format (you can use libraries like moment.js for this)
    // For example:
    return new Date(timestamp).toLocaleString(); // Change the formatting as per your requirements
  },
    fetchUsers() {
      axios
        .get('http://localhost:8000/api/v1/users/')
        .then((response) => {
          const sortedUsers = response.data.sort((a, b) => b.followers_count - a.followers_count);

          // Get the top users excluding the current user
          this.filteredUsers = sortedUsers.filter((user) => user.username !== this.username);
        })
        .catch((error) => {
          console.error('Error fetching users:', error.response.data);
        });
    },
    selectReceiver(recevier_id, recevier_name) {
      this.recevier_isSelected = !this.recevier_isSelected

      this.recevier_id = recevier_id
      this.recevier_name = recevier_name

      this.fetchMessages(recevier_id)
    },

    async fetchMessages(rid) {
      const receiverId = rid; 
      const senderId = this.userId;

    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v3/chat/', {
      params: {    
        sender: senderId,
        receiver: receiverId,
      }
    });
      this.messages = response.data;
      // this.senderMessages = [];
      // this.receiverMessages = [];      
      this.messages.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));
      // // Separate sender and receiver messages
      // messages.forEach((message) => {
      //   if (message.receiver.id === receiverId) {
      //     this.senderMessages.push(message);       
      //   } else if (message.sender.id === receiverId){       
      //     this.receiverMessages.push(message);      
      //   }
      // });

    } catch (error) {
      console.error('Error fetching messages:', error);
    }
  },
   async sendMessage() {
      try {
       
        const receiverId = this.recevier_id; 
        const content = this.content; 
        const senderId = this.userId; 
        
        // Make the API call to send the message
        const response = await axios.post('http://localhost:8000/api/v3/chat/', {
          sender: senderId,
          receiver: receiverId,
          content: content,
        });

        // Clear the message input field or do any other necessary actions
        this.content = '';
        // this.receiverName = response.data.receiver.username;
        // this.senderName = response.data.sender.username;
        // this.senderMessage = response.data.content;
        console.log('Message successfully sent:', response.data.content);
        // window.location.reload();
        this.fetchMessages(receiverId)      
      } catch (error) {
        console.error('Error sending message:', error);
      }
    },
    getFirstLetter(username) {
      return username.charAt(0).toUpperCase();
    },

    // Send on enter button press

     sendEnter(event) {
      if (event.key === 'Enter') {
        this.sendMessage();
      }
    }
  },
};
</script>

