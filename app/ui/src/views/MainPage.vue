<template>
  <div class="mainpage">

    <Notification messg="Novy projekt bol vytvoreny" format="2" v-if="this.NotifEventCreated" />
    <Notification messg="Projekt bol pridany do oblubenych" format="2" v-if="this.NotifFavorite" />
    <Notification messg="Taky projekt neexistuje" format="1" v-if="this.NotifError" />

    <Modal v-show="isModalVisible" @close="closeModal" />

    <div class="search">
    <input type="text" class="searchbar" placeholder="Vyhladat..." v-model="searchValue" />
    <button style="margin-left: 1rem" class="filters" @click="searchBar()">{{ $t("MainPage.Search") }}</button>
    <button class="create" type="button" @click="showModal">{{$t("MainPage.Create") }}</button>
    </div>
    
    <div class="dashboard"> {{ $t("MainPage.Filter") }}
      <button class="filters" @click="sortEvents2('2')">{{ $t("Difficulty.Newest") }}</button>
      <button class="filters" style="margin-right:2rem" @click="redirectFavorite">{{ $t("MainPage.Favorite") }}</button><span class="vl"></span>
      <button class="filters" @click="sortEvents2('1')">{{ $t("Difficulty.Beginner") }}</button>
      <button class="filters" @click="sortEvents2('3')">{{ $t("Difficulty.Advanced") }}</button>
      <button class="filters" @click="sortEvents2('3')">{{ $t("Difficulty.Expert") }}</button>
    </div>
    
    <div class="dashboard" style="margin-top: 1rem">
      <button class="filters" style="background-color:#f8cee0" @click="sortEvents('sport')">{{ $t("Technologie.Angular") }}</button>
      <button class="filters" style="background-color:#d1e5f8" @click="sortEvents('entertainment')">{{ $t("Technologie.Java") }}</button>
      <button class="filters" style="background-color:#eff57c" @click="sortEvents('music')">{{ $t("Technologie.Python") }}</button>
      <button class="filters" style="background-color:#c8c3f8" @click="sortEvents('travelling')">{{ $t("Technologie.React") }}</button>
      <button class="filters" style="background-color:#6c5676; color:#fff" @click="sortEvents('food')">{{ $t("Technologie.Cplus") }}</button>
      <button class="filters" style="background-color:#bfef88" @click="sortEvents('education')">{{ $t("Technologie.Csharp") }}</button>
      <button class="filters" style="background-color:#f8b184" @click="sortEvents('other')">{{ $t("Technologie.JavaScript") }}</button>
    </div>

    <div class="event-list">
      <h2 style="text-indent: 3rem;">{{ $t("MainPage.List") }}</h2>
      <ul>
        <li v-for="event in events2" :key="event.EventId" class="event-list">
          <div class="box" :class="(event.EventFilter)">
            <router-link :to="'/detailevent/' + event.EventId">
              <img
              :src="PhotoPath + event.EventName + format"
              class="event-image"
              @error="replaceByDefault"/>
            </router-link>
              
            <img src="../images/heart-icon-white.jpg" class="heart-image" @click="addFavorite(event.EventId)" v-if="this.user != null && this.user != 'null'">
                        
            <router-link :to="'/detailevent/' + event.EventId">
              <div>
                <span class="event-name"> {{ event.EventName }} </span>
                <span class="grey-text-right"  
                  >{{ getUsersCount(event.EventSignedUsers) }}/{{
                    event.EventMaxUsers
                  }}</span
                ><br />
                {{ event.EventAddress }}<br />
                {{ event.EventDateOfEvent }}<span class="grey-text-right" style="color:#8f8f8f">#{{event.EventId}}</span>
              </div>
            </router-link>
          </div>
        </li>
      </ul>
    </div>

    <vue-awesome-paginate
    :total-items=this.events.length
    :items-per-page="15"
    :max-pages-shown="5"
    :current-page="1"
    :on-click="onClickHandler"
    style="justify-content: center; display: flex"
    v-if="this.events.length>15"
  />

  <div v-if="this.events.length==0" style="text-indent: 3rem;">{{ $t("MainPage.NoEvents") }}</div>

    <div class="event-list">
    <h2 style="text-indent: 3rem">{{ $t("MainPage.Friends") }}</h2>
    <ul class="scrollmenu">
      <li v-for="user in users" :key="user.UserName" class="scroll-friends">        
          <div class="friend-box">
            <router-link :to="'/profile/' + user.UserName"><img :src="PhotoPath + user.UserName + format" class="friend-pfp" @error="replaceByDefault" /><br>
            <div style="font-weight: 525; font-size: 1.25rem;">{{user.UserName}}</div></router-link>
            <button class="filters friends-btn">{{ $t("MainPage.Add") }}</button>
          </div>          
      </li>    
    </ul>
    </div>

  </div>
</template>

<script>
import axios from "axios";
import Modal from "./AddNewEventModal.vue";
import Notification from "./Notification.vue";

export default {
  name: "MainPage",
  components: {
    Notification,
    Modal,
  },
  data() {
    return {
      events: [],
      events2:[],
      users:[],
      isModalVisible: false,
      PhotoPath: "http://127.0.0.1:8000/Photos/",
      format: ".jpg",
      user: "null",
      NotifEventCreated: false,
      NotifFavorite: false,
      NotifError: false
    };
  },
  methods: {
    resetNotif(){
      this.NotifEventCreated=false
      this.NotifFavorite=false
      this.NotifError=false
    },
    getUsersCount(abc){
      let temp = abc.split(",")
      temp = temp.filter(function (e) {return e !== ""});
      return temp.length
    },
    searchBar(){
      if(isNaN(this.searchValue)) {
        axios.get("http://127.0.0.1:8000/eventikk/" + this.searchValue).then((response)=> {
          this.$router.push("detailevent/"+response.data);
        }).catch(
          
            this.NotifError=true
          )
      }
      else this.$router.push("detailevent/"+this.searchValue);
    },
    addFavorite(id){
      this.resetNotif()
      axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response)=> {
        let tempUser = response.data[0].UserFavorites.split(",")
        tempUser.push(id.toString())
        tempUser = tempUser.filter(function (e) {return e !== ""});
        axios.put("http://127.0.0.1:8000/pokus/" + this.user, {
          UserId: response.data[0].UserId,
          UserName: response.data[0].UserName,
          UserAddress: response.data[0].UserAddress,
          UserDescription: response.data[0].UserDescription,
          UserEvents: response.data[0].UserEvents,
          UserFavorites: tempUser.toString(),
          UserFriends: response.data[0].UserFriends,
          UserOwnedEvents: response.data[0].UserOwnedEvents
          });
        })
        this.NotifFavorite = true
    },
    sortEvents2(type){
      this.events2=[],
      this.events=[],
      axios.get("http://127.0.0.1:8000/order/"+type).then((response) => {
        this.events = response.data;
        for (let i = 0; i < 15; i++) {
          if( this.events[i]!=undefined)
            this.events2.push(this.events[i])
        } 
      });
    },
    sortEvents(type){
      this.events2=[],
      this.events=[],
        axios.get("http://127.0.0.1:8000/eventik/"+type).then((response) => {
        this.events = response.data;
        for (let i = 0; i < 15; i++) {
          if( this.events[i]!=undefined)
            this.events2.push(this.events[i])
        } 
      });
    },
    onClickHandler(a){
      this.events2 = []
      for (let i = 15*(a-1); i < 15*(a-1)+15; i++) {
        if(this.events[i]!=undefined){
          this.events2.push(this.events[i])
          }
      } 
    },
    redirectFavorite(){
      this.$router.push("favorite");
    },
    replaceByDefault(e) { 
      e.target.src = "http://127.0.0.1:8000/Photos/NoPhoto.jpg";
    },
    getEvents() {
      axios.get("http://127.0.0.1:8000/events").then((response) => {
        this.events = response.data;
        for (let i = 0; i < 15; i++) {
          if( this.events[i]!=undefined)
            this.events2.push(this.events[i])
        } 
      });
    },
    getUsers() {
      axios.get("http://127.0.0.1:8000/users").then((response) => {
        this.users = response.data;
      });
    },
    showModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.resetNotif()
      this.isModalVisible = false;
      this.events2=[]
      this.events=[]
      this.getEvents()
      this.NotifEventCreated = true
    },
  },
  mounted: function () {
    this.user = localStorage.getItem("user-storage").replace(/['"]+/g, "");
    this.getEvents();
    this.getUsers();
  },
};
</script>

<style>
body{
  margin: 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.mainpage{
  text-align: center;
}

.search{
  display: flex;
  justify-content: center;
}

.searchbar{
  width:25%;
  border-bottom: 1px solid #020381;
  padding: 5px;
  margin-left: 2rem;
  outline: none;
}

.sport{
  border-bottom: 5px solid #f8cee0;
}

.entertainment{
  border-bottom: 5px solid #d1e5f8;
}

.music{
  border-bottom: 5px solid #eff57c;
}

.travelling{
  border-bottom: 5px solid #c8c3f8;
}

.food {
  border-bottom: 5px solid #6c5676;
}

.education{
  border-bottom: 5px solid #bfef88;
}

.other{
  border-bottom: 5px solid #f8b184;
}


.event-list {
  list-style-type: none;
  display: inline-block;
}

.event-name {
  font-weight: bold;
  font-size: 20px;
}

.event-image {
  aspect-ratio: calc(16 / 8);
  float: center;
  border-radius: 0.3rem;
  width: 100%;
  min-height: 100px;
  /*outline: 3px solid #020381;*/
  box-shadow: #020381;
  margin-bottom: 0.42rem;
  object-fit: cover;
}

.box:hover {
  transform: scale(1.07);
  cursor: pointer;
}

.box {
  aspect-ratio: 69%;
  background-color: #dceeea;
  border-radius: 0.3rem;
  width: 18vw;
  min-width: 13.5rem !important;
  margin: 0.42rem;
  padding: 0.72rem;
  line-height: 1.2rem !important;
  transition: transform 0.4s;
  white-space: nowrap;
  overflow: hidden !important;
  text-overflow: ellipsis;
  object-fit: cover;
}

.grey-text-right {
  text-align: right;
  float: right;
  /*color: #8f8f8f;*/
}

.dashboard{
  font-weight: bolder;
  font-size: 1.2rem;
  margin-top: 1rem !important;
  text-align: center;  
}

.filters{
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  background-color: #2874FC;
  color: #2c3e50;
  margin: 0 0.8% 0 0.8%;
}

.filters:hover{
  background-color: #d0e4df;
  color: #2c3e50;
}

.vl {
  border-left: 2.5px solid #2c3e50;
  height: 3rem;
  position: absolute;
  z-index: -1;
}

.friend-box {
  outline: 3px solid #dceeea;
  aspect-ratio: calc(6/8);
  border-radius: 0.7rem;
  width: 10vw;
  min-width: 10rem;
  margin: 0.6rem;
  padding: 1.1rem;
  line-height: 20px;
  white-space: nowrap;
  overflow: hidden !important;
  text-overflow: ellipsis;
  object-fit: cover;
  text-align: center;
}

.friend-pfp {
  aspect-ratio: 1;
  width: 90%;
  float: center;
  border-radius: 50%;
  min-height: 7rem;
  min-width: 7rem;
  outline: 3px solid #020381;
  margin-bottom: calc(0.7rem);
  object-fit: cover;
}

.scroll-friends{
  list-style-type: none;
  display: inline-block;
  overflow: auto;
}

.scrollmenu{
  overflow: auto;
  white-space: nowrap;
  width: 92vw;
  margin-left: 2.6%;
  padding-left: 0;
  scrollbar-color: #020381 #dceeea;
}

.filters.friends-btn{
  height: 30px;
  line-height: 0.1;
  margin-top: 0.7vw;
}

.filters.friends-btn:focus{
  background-color: transparent;
}

.heart-image{
  aspect-ratio: 1;
  height: 2.2rem;
  position: relative;
  right: 2.2rem;
  bottom: 0.4rem;
}


.heart-image:hover{
  content: url('../images/heart-icon-red.jpg');
  aspect-ratio: 1;
  height: 2.2rem;
  position: relative;
  right: 2.2rem;
  bottom: 0.4rem;
}

.create{
  background-color: #020381;
  margin-left: 2rem;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

</style>