<template>
  <div class="profile-page">
    <div class="profile-box">
      <img
        :src="PhotoPath + singleUser.username + format"
        class="profile-picture"
        @error="replaceByDefault"
      />
      <span>
        <img src="../images/edit-icon.jpg" class="add-remove-friend-img edit-i" style="width: calc(1.6rem + 0.7vw);" v-if="this.user == singleUser.username" @click="redirecteditprofile"/>

        <img src="../images/add-contact-icon.jpg" class="add-remove-friend-img add-frnd" @click="addFriend" v-if="!(this.user == singleUser.username) && !this.added"/>

        <img src="../images/contact-added-icon.jpg" class="add-remove-friend-img rmv-frnd" @click="removeFriend" v-if="!(this.user == singleUser.username) && this.added"/>

        <span class="name">{{ singleUser.username }}</span
        ><br />
        {{ singleUser.email }}<br />
        {{ formatDate(singleUser.last_login) }} </span
      ><br />
    </div>
    <div>{{ singleUser2.UserDescription }}<br>
    
    </div>

    <hr />
    <span class="text-buttons" @click="owned()"> {{ $t("Profile.Owned") }}</span>
    <span class="text-buttons" @click="joined()"> {{ $t("Profile.Joined") }}</span>
    <span class="text-buttons" @click="friends()"> {{ $t("Profile.Friends") }}</span>
  </div>

  <ul class="three-events" v-if="this.version==1">
    <li v-for="event in ownedEvents2 /*signedEvents,ownedEvents*/" :key="event.EventId" class="event-list">
    <router-link :to="'/detailevent/' + event.EventId">
      <div class="box">
        <img
          :src="PhotoPath + event.EventName + format"
          class="event-image"
          @error="replaceByDefault"
        /><br />
        <span class="event-name"> {{ event.EventName }} </span>
        <span class="grey-text-right"
          >{{ event.EventSignedUsers.split(",").length }}/{{ event.EventMaxUsers }}</span
        ><br />
        {{ event.EventAddress }}<br />
        {{ event.EventDesciption }}
      </div>
      </router-link>
    </li>
  </ul>

  <vue-awesome-paginate
  v-if="this.version==1 && this.ownedEvents.length>9"
    :total-items=this.ownedEvents.length
    :items-per-page="9"
    :max-pages-shown="3"
    :current-page="1"
    :on-click="onClickHandler"
    style="display: flex; justify-content: center"
  />

  <p v-if="this.version==1 && this.ownedEvents.length==0" style="text-align: center;">{{ $t("Profile.NoCreatedEvent") }}</p>

    <ul class="three-events" v-if="this.version==2">
    <li v-for="event in signedEvents2 /*signedEvents,ownedEvents*/" :key="event.EventId" class="event-list">
    <router-link :to="'/detailevent/' + event.EventId">
      <div class="box">
        <img
          :src="PhotoPath + event.EventName + format"
          class="event-image"
          @error="replaceByDefault"
        /><br />
        <span class="event-name"> {{ event.EventName }} </span>
        <span class="grey-text-right"
          >{{ event.EventSignedUsers.split(",").length }}/{{ event.EventMaxUsers }}</span
        ><br />
        {{ event.EventAddress }}<br />
        {{ event.EventDesciption }}
      </div>
      </router-link>
    </li>
  </ul>

    <vue-awesome-paginate
  v-if="this.version==2 && this.signedEvents.length>9" 
    :total-items=this.signedEvents.length
    :items-per-page="9"
    :max-pages-shown="3"
    :current-page="1"
    :on-click="onClickHandler2"
    style="display: flex; justify-content: center"
  />

  <p v-if="this.version==2 && this.signedEvents.length==0" style="text-align: center;">{{ $t("Profile.NoSignedEvent") }}</p>

  <ul class="three-events" v-if="this.version==3">
      <li v-for="friend in friendList" :key="friend.UserId" class="scroll-friends">
          <div class="friend-box">
            <router-link :to="'/profile/' + friend.UserName">
            <img :src="PhotoPath + friend.UserName + format" class="friend-pfp" @error="replaceByDefault" /><br>
            <div style="font-weight: 525; font-size: 1.25rem;">{{friend.UserName}}</div>
            </router-link>
            <button class="filters friends-btn">{{ $t("Profile.Remove") }}</button>
          </div>          
      </li>    
    </ul>

    <div v-if="this.version==3 && this.friendList.length==0" style="text-align: center;">{{ $t("Profile.NoFriends") }}/</div>

  <div v-if="this.version==4">

    <form @submit.prevent="editProfile">
      <label>{{ $t("Profile.Photo") }}</label>
      <input type="file" id="image" v-on:change="onFileChange" />

      <label>{{ $t("Profile.Description") }}</label>
      <input type="text" v-model="UserDescription" />

      <label>{{ $t("Profile.Address") }}</label>
      <input type="text" v-model="UserAddress" />

      <label>{{ $t("Profile.Email") }}</label>
      <input type="mail" v-model="UserEmail" /><br>

      <button type="submit">{{ $t("Profile.ChangeData") }}</button>
    </form>
  </div>

      

</template>

<script>
import axios from "axios";
import moment from "moment";

export default {
  name: "DetailEvent",
  components: {},
  data() {
    return {
      singleUser: [],
      singleUser2: [],
      events: [],
      ownedEvents:[],
      ownedEvents2:[],
      signedEvents:[],
      signedEvents2:[],
      friendList:[],
      PhotoPath: "http://127.0.0.1:8000/Photos/",
      format: ".jpg",
      user: "null",
      version : 1,
      added: false,
      UserDescription: "a",
      UserAddress: "a",
      UserEmail: "a",
    };
  },
  methods: {
    editProfile() {      
        let formData=new FormData();
        formData.append('file',this.photo[0]);

        axios.post("http://127.0.0.1:8000/events/savefile/"+this.$route.params.name,formData).then(()=>{
        });

            axios.put("http://127.0.0.1:8000/user/" + this.$route.params.id, {
        id: this.singleUser.id,
        password: this.singleUser.password,
        last_login: this.singleUser.last_login,
        is_superuser: this.singleUser.is_superuser,
        username: this.singleUser.username,
        first_name: this.singleUser.first_name,
        last_name: this.singleUser.last_name,
        email: this.UserEmail,
        is_staff: this.singleUser.is_staff,
        is_active: this.singleUser.is_active,
        date_joined: this.singleUser.date_joined
      });

      axios.put("http://127.0.0.1:8000/pokus/" + this.$route.params.id, {
        UserId: this.singleUser2.UserId,
        UserName: this.singleUser2.UserName,
        UserAddress: this.UserAddress,
        UserDescription: this.UserDescription,
        UserEvents: this.singleUser2.UserEvents,
        UserFavorites: this.singleUser2.UserFavorites,
        UserFriends: this.singleUser2.UserFriends,
        UserOwnedEvents: this.singleUser2.UserOwnedEvents
      });
      this.version=2
      this.getUserInfo();
    },
    onFileChange(e) {
      this.photo = e.target.files;
    },
     onClickHandler(a){
      this.ownedEvents2 = []
      for (let i = 9*(a-1); i < 9*(a-1)+9; i++) {
        if(this.ownedEvents[i]!=undefined){
          this.ownedEvents2.push(this.ownedEvents[i])
          }
      } 
    },
    onClickHandler2(a){
      this.signedEvents2 = []
      for (let i = 9*(a-1); i < 9*(a-1)+9; i++) {
        if(this.signedEvents[i]!=undefined){
          this.signedEvents2.push(this.signedEvents[i])
          }
      } 
    },
    addFriend(){
      axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response) => {

          let abc = response.data[0].UserFriends.split(",")
          abc.push(this.$route.params.name)       
           axios.put("http://127.0.0.1:8000/pokus/" + this.user, {
                  UserId: response.data[0].UserId,
                  UserName: response.data[0].UserName,
                  UserAddress: response.data[0].UserAddress,
                  UserDescription: response.data[0].UserDescription,
                  UserEvents: response.data[0].UserEvents,
                  UserFavorites: response.data[0].UserFavorites,
                  UserFriends: abc.toString(),
                  UserOwnedEvents: response.data[0].UserOwnedEvents
                });
        });
    },
    removeFriend(){
      axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response) => {

          let abc = response.data[0].UserFriends.split(",")
          let k = this.$route.params.name
          let filteredArray = abc.filter(function (e) {return e !== k});   
           axios.put("http://127.0.0.1:8000/pokus/" + this.user, {
                  UserId: response.data[0].UserId,
                  UserName: response.data[0].UserName,
                  UserAddress: response.data[0].UserAddress,
                  UserDescription: response.data[0].UserDescription,
                  UserEvents: response.data[0].UserEvents,
                  UserFavorites: response.data[0].UserFavorites,
                  UserFriends: filteredArray.toString(),
                  UserOwnedEvents: response.data[0].UserOwnedEvents
                });
        });
    },
    owned(){
      this.version = 1
    },
    joined(){
      this.version = 2
    },
    friends(){
      this.version = 3
    },
    redirecteditprofile() {
      //this.$router.push("editprofile/" + this.user);
      this.version = 4
    },
    replaceByDefault(e) {
      e.target.src = "http://127.0.0.1:8000/Photos/NoPhoto.jpg";
    },
    formatDate(value) {
      if (value) {
        return moment(String(value)).format("MM/DD/YYYY hh:mm");
      }
    },
    getUserInfo() {
      axios.get("http://127.0.0.1:8000/user/" + this.$route.params.name).then((response) => {
          this.singleUser = response.data[0];
          this.UserEmail = this.singleUser.email;
          });
          axios.get("http://127.0.0.1:8000/pokus/" + this.$route.params.name).then((response) => {
          this.singleUser2 = response.data[0];
          let abc = response.data[0].UserOwnedEvents.split(",")
          this.UserAddress = this.singleUser2.UserAddress;
          this.UserDescription = this.singleUser2.UserDescription;
          for (const item in abc){
              axios.get("http://127.0.0.1:8000/events/" + abc[item]).then((response) => {
                  this.ownedEvents.push(response.data[0])
                  
                    if (abc[item]==abc.at(-1)){
                        
                      for (let i = 0; i < 9; i++) {
                          if( this.ownedEvents[i]!=undefined)
                          this.ownedEvents2.push(this.ownedEvents[i])
                          //console.log(this.ownedEvents[i])
                      }

                      //console.log(JSON.stringify(this.ownedEvents, null, 2))
                    }
                });

            }




          let def = response.data[0].UserEvents.split(",")
          for (const itemm in def){
              axios.get("http://127.0.0.1:8000/events/" + def[itemm]).then((response) => {
                  this.signedEvents.push(response.data[0])
                      
                      if (def[itemm]==def.at(-1)){
                        
                      for (let i = 0; i < 9; i++) {
                        if( this.signedEvents[i]!=undefined)
                          this.signedEvents2.push(this.signedEvents[i])
                          //console.log(this.ownedEvents[i])
                      }
                    }

                });
            }
          let ghi = response.data[0].UserFriends.split(",")
          for (const itemmm in ghi){
              axios
                .get("http://127.0.0.1:8000/pokus/" + ghi[itemmm])
                .then((response) => {
                  this.friendList.push(response.data[0])
                });
            }
        });
    },
    getEvents() {
      axios.get("http://127.0.0.1:8000/events").then((response) => {
        this.events = response.data;
      });
    },
    checkAdded(){
      axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response) => {
        let tempList = response.data[0].UserFriends.split(",")
        if (tempList.includes(this.$route.params.name)) {
          this.added = true
        }
      })
    }
  },
  mounted: function () {
    this.getEvents();
    this.getUserInfo();
    this.user = localStorage.getItem("user-storage").replace(/['"]+/g, "");
    this.checkAdded();
  },
};
</script>

<style>
.profile-page {
  margin: 0 3% 0 3%;
  text-align: center;
}

.profile-picture {
  aspect-ratio: 1;
  float: left;
  border-radius: 50%;
  width: 25%;
  min-height: 150px;
  min-width: 150px;
  outline: 3px solid #020381;
  margin-right: 40px;
  object-fit: cover;
}

.profile-box {
  font-size: calc(15px + 0.25vw);
  float: center;
  text-align: left;
  aspect-ratio: 70%;
  max-width: 35vw;
  min-width: 450px !important;
  margin: 0 auto;
  padding: 12px;
  line-height: calc(20px + 0.8vw);
  display: flex;
  justify-content: center;
  word-break: break-word;
  margin-bottom: 15px;
  object-fit: cover;
}

.profile-box span {
  align-self: flex-end;
  margin-bottom: 0.3vw;
}

.three-events {
  margin: 15px 19vw 0 19vw;
}

.name {
  font-size: xx-large;
  font-weight: lighter;
}

hr {
  border: 0.8px solid rgb(195, 221, 216);
  margin: 15px 19vw 10px 19vw;
}

.text-buttons {
  margin: 0 5rem 0 5rem;
  cursor: pointer;
}

.add-remove-friend-img{
  float: right;
  width: calc(2rem + 0.7vw);
  height: auto;
}

.add-remove-friend-img:hover{
  cursor: pointer;
}

.add-frnd:hover{
  content: url('../images/add-contact-icon-hover.jpg');
}

.rmv-frnd:hover{
  content: url('../images/remove-contact-icon.jpg');
}

.edit-i:hover{
  content: url('../images/edit-icon-hover.jpg');
}
</style>