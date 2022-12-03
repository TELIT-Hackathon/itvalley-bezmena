<template>
  <div class="detailevent">
    <Notification messg="Ziaden user" format="1" v-if="this.NotifNoUser" />
    <Notification messg="Pohodka zapisal som ta" format="2" v-if="this.NotifSuccessSign" />
    <Notification messg="Odstraneny" format="2" v-if="this.NotifRemoved" />
    <Notification messg="Koment bol pridany" format="2" v-if="this.NotifKoment" />
    <Notification messg="Koment bol vymazany" format="2" v-if="this.NotifKomentDeleted" />
    <Notification messg="Udaje boli zmenene" format="2" v-if="this.NotifData" />
    <Notification messg="Event uz je plny" format="1" v-if="this.NotifFull" />

    

    <div style="display: flex; min-height: 160px;">
      <div class="images">
        <img :src="PhotoPath + singleEvent.EventName + format" @error="replaceByDefault" class="detail-image"/>    
      </div>
      <div class="info-right">

        <button v-if="this.user != null && this.user != 'null' && !this.UserSigned && this.owner!=this.user" @click="subUserToEvent()" class="detail-buttons">
          {{ $t("DetailEvent.SignIn") }}
        </button>
        <button v-if="this.user != null && this.user != 'null' && this.UserSigned && this.owner!=this.user" @click="deleteUserFromEvent(this.user)" class="detail-buttons">
          {{ $t("DetailEvent.SignOut") }}
        </button>      
        <a href="#edit-event-anchor"><img src="../images/edit-icon.jpg" @click="redirecteditevent()" 
        v-if="this.user == this.owner" class="add-remove-friend-img edit-i" style="width: calc(1.6rem + 0.7vw);float:none;margin-right: 1.5rem"/></a>

        
      
        <img src="../images/heart-icon-white.jpg" class="heart-image" style="left: 1rem; top: 0.6rem; margin-right: 2rem;" 
          v-if="this.user != null && this.user != 'null' && !this.UserFavorite && this.owner!=this.user" @click="addToFavorite()">
        <img src="../images/heart-icon-red.jpg" class="heart-image" style="left: 1rem; top: 0.6rem; margin-right: 2rem;" 
          v-if="this.user != null && this.user != 'null' && this.UserFavorite && this.owner!=this.user" @click="removeFromFavorite(this.user)">
        <br>

        <h1 style="margin: 0; margin-bottom: 1rem">{{ singleEvent.EventName }}<span style="font-size:16pt; font-weight: lighter;"> #{{ singleEvent.EventId }}</span></h1>        

        <b>{{ $t("DetailEvent.Owner") }}:</b> {{ singleEvent.EventOwner }}  <br />
        <b>{{ $t("DetailEvent.Date") }}:</b> {{ singleEvent.EventDateOfEvent }} <br />
        <b>{{ $t("DetailEvent.Address") }}:</b> {{ singleEvent.EventAddress }} <br />
        
          
      </div>
    </div>

    <div>
    <b>{{ $t("DetailEvent.Description") }}:</b> {{ singleEvent.EventDescription }}</div><br>    
      {{ $t("DetailEvent.SignedUsers") }}: {{ this.arr.length }}/{{ singleEvent.EventMaxUsers }}
    
    
    <div class="signed-users">
    <div v-for="item in arr" :key="item.message">
      <router-link :to="'/profile/' + item">{{ item }}</router-link>
      <button @click="deleteUserFromEvent(item)" v-if="this.user == singleEvent.EventOwner" class="btn-delete-user">
        X
      </button>      
    </div>
  </div>
    <span v-if="this.arr.length==0">{{ $t("DetailEvent.NoUser") }}</span>

  <div v-if="this.editing">
    <form @submit.prevent="editEvent" id="edit-event-anchor">
      <label>{{ $t("DetailEvent.Photo") }}</label>
      <input type="file" id="image" v-on:change="onFileChange" />

      <label>{{ $t("DetailEvent.Description") }}</label>
      <input type="text" v-model="EventDescription" />

      <label>{{ $t("DetailEvent.Date") }}</label>
      <input type="date" v-model="EventDate" />

      <label>{{ $t("DetailEvent.Capacity") }}</label>
      <input type="number" v-model="EventMaxUsers" />

      <label>{{ $t("DetailEvent.Address") }}</label>
      <input type="text" v-model="EventAddress" /><br>
      
      <button type="submit">{{ $t("DetailEvent.ChangeData") }}</button>
      <img src="../images/trash-icon.jpg"  v-if="this.user == this.owner" class="add-remove-friend-img trsh" style="width: calc(1.6rem + 0.7vw);float:right"/>
      <span style="float:right; margin: 0.5rem 0.4rem; cursor: pointer" @click="deleteEvent()">{{ $t("DetailEvent.DeleteEvent") }}</span>
      
    </form>
  </div>


    <form @submit.prevent="AddComment" style="max-width: 90vw !important; padding: 0 0 2rem 0">
      <label>{{ $t("DetailEvent.AddComment") }}</label>
      <input type="text" v-model="CommentText" required />
      <button class="submit" type="submit" style="margin-top:0.7rem">{{ $t("DetailEvent.Add") }}</button>      
    </form>

    <div>
      <h3>{{ $t("DetailEvent.AllComments") }}</h3>

        <p v-if="this.comments.length==0">{{ $t("DetailEvent.NoComments") }}</p>
        <div v-for="comment in comments" :key="comment.CommentId">
            <div class="comment-box">
              <img :src="PhotoPath + comment.CommentOwner + format" class="profile-picture-small" style="width:3.5rem; height: 3.5rem; margin:0 0.7rem 0 0.5rem" @error="replaceByDefault" />
              <div style="margin-bottom:1rem; display: inline-block;align-self: flex-end;">
                {{comment.CommentOwner}}<br> 
                <span style="color: #aaa">{{comment.CommentDate}}</span>
              </div><br>
              <div style="display: inline-flex; float: left;">
                <div style="width:75%; width: 60vw">{{ comment.CommentText }}</div>
                <div style="width:25%">
                  <span class="like-trash" style="margin:0.7rem 4.3rem 0 0">{{comment.CommentLikes.split(",").length}}</span>
                  <element class="like-green" @click="addLike(comment.CommentId)"><img src="../images/like-icon.jpg" class="like-trash like"></element>
                  <element v-if="this.user == comment.CommentOwner || this.user == singleEvent.EventOwner" class="trash-red" @click="deleteComment(comment.CommentId)">
                  <img src="../images/trash-icon.jpg" class="like-trash"></element>
                </div>
              </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Notification from "./Notification.vue";

export default {
  name: "DetailEvent",
  components: {
    Notification,
  },
  data() {
    return {
      singleEvent: [],
      eventN: "",
      user: "null",
      arr: [],
      comments:[],
      NotifNoUser: false,
      NotifSuccessSign: false,
      NotifRemoved: false,
      NotifKoment: false,
      NotifKomentDeleted: false,
      NotifFull:false,
      NotifData: false,
      PhotoPath: "http://127.0.0.1:8000/Photos/",
      format: ".jpg",
      UserFavorite: false,
      UserSigned: false,
      owner: "",
      editing: false,
      TEventPhoto: null,
      TEventDescription: null,
      TEventDate: null,
      TEventMaxUsers: null,
      TEventAddress: null,
      EventPhoto: "fotka",
      EventDescription: "aaaaaa",
      EventDate: "a",
      EventMaxUsers: "a",
      EventAddress: "a",
    };
  },
  methods: {
    onFileChange(e) {
      this.photo = e.target.files;
    },
    editEvent() {
      this.resetNotif()
      this.EventAddress == null
        ? (this.TEventAddress = this.singleEvent.EventAddress)
        : (this.TEventAddress = this.EventAddress);
      this.EventDescription == null
        ? (this.TEventDescription = this.singleEvent.EventDescription)
        : (this.TEventDescription = this.EventDescription);
      this.EventMaxUsers == null
        ? (this.TEventMaxUsers = this.singleEvent.EventMaxUsers)
        : (this.TEventMaxUsers = this.EventMaxUsers);
      this.EventDate == null
        ? (this.TEventDate = this.singleEvent.EventDateOfEvent)
        : (this.TEventDate = this.EventDate);

      
        let formData=new FormData();
        formData.append('file',this.photo[0]);

        axios.post("http://127.0.0.1:8000/events/savefile/"+this.singleEvent.EventName,formData).then(()=>{
        });

      axios.put("http://127.0.0.1:8000/events/" + this.$route.params.id, {
        EventId: this.singleEvent.EventId,
        EventName: this.singleEvent.EventName,
        EventAddress: this.TEventAddress,
        EventDescription: this.TEventDescription,
        EventOwner: this.user,
        EventDateOfCreate: this.singleEvent.EventDateOfCreate,
        EventDateOfEvent: this.TEventDate,
        EventMaxUsers: this.EventMaxUsers,
        EventSignedUsers: this.singleEvent.EventSignedUsers,
        EventFilter: this.singleEvent.EventFilter,
      });
      this.getEventInfo()
      this.editing=false
      this.NotifData=true
    },
    resetNotif(){
      this.NotifNoUser=false
      this.NotifSuccessSign=false
      this.NotifRemoved=false
      this.NotifKomentDeleted=false
      this.NotifKoment=false
      this.NotifData=false
      this.NotifFull=false
    },
    addLike(id){
      axios.get("http://127.0.0.1:8000/komment/" + id).then((response)=> {
        let abc = response.data[0].CommentLikes.split(",")
        if(!abc.includes(this.user)){
          abc.push(this.user)
          axios.put("http://127.0.0.1:8000/komment/" + id,{
                  CommentId: response.data[0].CommentId,
                  EventId: response.data[0].EventId,
                  CommentText: response.data[0].CommentText,
                  CommentOwner: response.data[0].CommentOwner,
                  CommentDate: response.data[0].CommentDate,
                  CommentLikes: abc.toString()
          })
        }
      })
    },
    deleteComment(id){
      this.resetNotif()
      this.comments = []
      axios.delete("http://127.0.0.1:8000/comment/" + id).then(() => {
        axios.get("http://127.0.0.1:8000/comment/" + this.$route.params.id).then((response) => {
        this.comments = response.data;
        })
      })
      this.NotifKomentDeleted=true
    },
    addToFavorite(){
      this.resetNotif()
      axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response)=> {
        let tempUser = response.data[0].UserFavorites.split(",")
        tempUser.push(this.singleEvent.EventId.toString())
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
        this.UserFavorite=true
        this.NotifSuccessSign=true
      },
      removeFromFavorite(){
        this.resetNotif()
        axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response)=> {
          let tempUser = response.data[0].UserFavorites.split(",")
          let temp = this.singleEvent.EventId.toString()
          let filteredArray = tempUser.filter(function (e) {return e !== temp});
          axios.put("http://127.0.0.1:8000/pokus/" + this.user, {
            UserId: response.data[0].UserId,
            UserName: response.data[0].UserName,
            UserAddress: response.data[0].UserAddress,
            UserDescription: response.data[0].UserDescription,
            UserEvents: response.data[0].UserEvents,
            UserFavorites: filteredArray.toString(),
            UserFriends: response.data[0].UserFriends,
            UserOwnedEvents: response.data[0].UserOwnedEvents
          })
        })
        this.UserFavorite=false
        this.NotifRemoved=true
      },
      AddComment() {
        this.resetNotif()
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, "0");
        var mm = String(today.getMonth() + 1).padStart(2, "0");
        var yyyy = today.getFullYear();
        today = yyyy + "-" + mm + "-" + dd;

        axios.post("http://127.0.0.1:8000/comment", {
          EventId: this.$route.params.id,
          CommentText: this.CommentText,
          CommentOwner: this.user,
          CommentDate: today,
          CommentLikes: ""
        })
        axios.get("http://127.0.0.1:8000/comment/" + this.$route.params.id).then((response) => {
            this.comments = response.data;
        });
        this.NotifKoment=true
      },
      deleteEvent() {
        axios.delete("http://127.0.0.1:8000/events/" + this.$route.params.id);
        this.$router.push("/");
      },
      redirecteditevent() {
        this.editing=true
        //this.$router.push("editevent/" + this.$route.params.id);
      }, 
      replaceByDefault(e) {
        e.target.src = "http://127.0.0.1:8000/Photos/NoPhoto.jpg";
      }, 
      deleteUserFromEvent(item) {
        this.resetNotif()
        axios.get("http://127.0.0.1:8000/events/" + this.$route.params.id).then((response) => {
          this.arr = response.data[0].EventSignedUsers.split(",");
          var filteredArray = this.arr.filter(function (e) {return e !== item;});
          response.data[0].EventSignedUsers = filteredArray.toString();
          axios.put("http://127.0.0.1:8000/events/" + this.$route.params.id,response.data[0]);
          this.arr = response.data[0].EventSignedUsers.split(",");
          this.arr = this.arr.filter(function (e) {return e !== ""});
          this.NotifRemoved = true;
          axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response)=> {
            let tempUser = response.data[0].UserEvents.split(",")
            let temp = this.singleEvent.EventId.toString()
            let filteredArray = tempUser.filter(function (e) {return e !== temp});
            axios.put("http://127.0.0.1:8000/pokus/" + this.user, {
              UserId: response.data[0].UserId,
              UserName: response.data[0].UserName,
              UserAddress: response.data[0].UserAddress,
              UserDescription: response.data[0].UserDescription,
              UserEvents: filteredArray.toString(),
              UserFavorites: response.data[0].UserFavorites,
              UserFriends: response.data[0].UserFriends,
              UserOwnedEvents: response.data[0].UserOwnedEvents
            })
          })
        });
        this.UserSigned=false
      },
      subUserToEvent() {
        this.resetNotif()
        if (this.user != null && this.user != "null") {
          axios.get("http://127.0.0.1:8000/events/" + this.$route.params.id).then((response) => {
            this.arr = response.data[0].EventSignedUsers.split(",");
            if(this.arr.length<response.data[0].EventMaxUsers){
              if (!this.arr.includes(this.user)) {
                response.data[0].EventSignedUsers = response.data[0].EventSignedUsers + "," + this.user;
                axios.put("http://127.0.0.1:8000/events/" + this.$route.params.id,response.data[0]);
                this.arr = response.data[0].EventSignedUsers.split(",");
                this.arr = this.arr.filter(function (e) {return e !== ""});
                axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response)=> {
                  let tempUser = response.data[0].UserEvents.split(",")
                  tempUser.push(this.singleEvent.EventId.toString())
                  tempUser = tempUser.filter(function (e) {return e !== ""});
                  axios.put("http://127.0.0.1:8000/pokus/" + this.user, {
                    UserId: response.data[0].UserId,
                    UserName: response.data[0].UserName,
                    UserAddress: response.data[0].UserAddress,
                    UserDescription: response.data[0].UserDescription,
                    UserEvents: tempUser.toString(),
                    UserFavorites: response.data[0].UserFavorites,
                    UserFriends: response.data[0].UserFriends,
                    UserOwnedEvents: response.data[0].UserOwnedEvents
                    });
                  })
                  this.NotifSuccessSign = true;
                  }
              }
              else {
                this.NotifFull=true;
                this.UserSigned=false
                return;
              }
            });
            } else {
            this.NotifNoUser = true;
          }
          this.UserSigned=true
      },
      getEventInfo() {
        //ZISKANIE INFO O EVENTE
        axios.get("http://127.0.0.1:8000/events/" + this.$route.params.id).then((response) => {
            this.singleEvent = response.data[0];
            this.arr = response.data[0].EventSignedUsers.split(",");
            this.arr = this.arr.filter(function (e) {return e !== ""});
            this.owner = response.data[0].EventOwner
                      this.EventPhoto = "fotka";
          (this.EventDescription = this.singleEvent.EventDescription),
            (this.EventDate = this.singleEvent.EventDateOfEvent),
            (this.EventMaxUsers = this.singleEvent.EventMaxUsers),
            (this.EventAddress = this.singleEvent.EventAddress);
        });
        axios.get("http://127.0.0.1:8000/comment/" + this.$route.params.id).then((response) => {
            this.comments = response.data;
        });
        axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response)=>{
          this.UserFavorite = response.data[0].UserFavorites.split(",").includes(this.$route.params.id)
          this.UserSigned = response.data[0].UserEvents.split(",").includes(this.$route.params.id)
        })
      },
    },
  mounted: function () {
    this.user = localStorage.getItem("user-storage").replace(/['"]+/g, "");
    this.getEventInfo();
  },
};
</script>

<style>
.detailevent {
  margin: 2.5vw 17vw 0 17vw;
  font-size: calc(10px + 0.6vw);
  text-align: left;
  white-space: initial;
  word-wrap: break-word;
}

.detail-image {
  outline: 4px solid #42b983;
  aspect-ratio: 2;
  float: left;
  object-fit: cover;
  margin-bottom: -5px;
  border-radius: 5px;
  width: 100%;
}

.images{
  border-radius: 5px;
  aspect-ratio: 2;
  width: 60%;
  margin-bottom: 18px;
  min-width: 300px;
  min-height: 150px;
}

.info-right{
  margin-left: 2rem;
  width: 40%;
}

.detail-buttons{
  font-size: calc(8px + 0.7vw);
  padding: 0.8rem 1.3rem; 
}

.btn-delete-user{
  font-size: 20px;
  padding: 10px;
  color: #4aae9b;
  background: transparent;
}

.signed-users{
  column-count: 4;
  column-gap: 40px;
  column-rule: 3px solid #dceeea;
  orphans: 1;
  margin-top: 1rem;
  line-height: 2rem;
}

.comment-box{
  outline: 2.5px solid #dceeea;
  border-radius: 0.3rem;
  margin: 0.5rem;
  margin-left: 0;
  padding: 0.9rem;
  line-height: 1.5rem;
  width: 65vw;
  display: flex;
  object-fit: cover;
  box-sizing: border-box;
  min-height: 100px;
  display: inline-block;
  position: relative;
}

.like-trash{
  width: 2.1rem;
  aspect-ratio: 1;
  margin: 0 0.5rem 0 0.5rem;
  top: 4.9rem;
  position: absolute;
  right:0.3rem;
  border-spacing: 20px;
}

.like-trash.like{
  right:2.9rem;
}

element.trash-red:hover{
  content: url('../images/trash-icon-red.jpg');
  cursor: pointer;
  width: 2.2rem;
  aspect-ratio: 1;
  margin: 0 0.5rem 0 0.5rem;
  position: absolute;
  right:0.3rem;
  border-spacing: 20px;
}

element.like-green:hover{
  content: url('../images/like-icon-green.jpg');
  cursor: pointer;
  width: 2.2rem;
  aspect-ratio: 1;
  margin: 0 0.5rem 0 0.5rem;
  position: absolute;
  right:2.9rem;
  border-spacing: 20px;
}

.trsh:hover{
  content: url('../images/trash-icon-red.jpg');
}
</style>