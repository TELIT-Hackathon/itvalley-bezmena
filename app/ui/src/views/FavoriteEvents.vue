<template>
  <div class="favoriteevents">


    <div class="event-list">
      <h2 style="text-indent: 3rem;">{{ $t("Other.ListOfFavorites") }}</h2>
      <ul>
        <li v-for="event in events" :key="event.EventId" class="event-list">
          <router-link :to="'/detailevent/' + event.EventId">
            <div class="box">
              <img
                :src="PhotoPath + event.EventName + format"
                class="event-image"
                @error="replaceByDefault"/>
                <br />
              <span class="event-name"> {{ event.EventName }} </span>
              <span class="grey-text-right"
                >{{ event.EventSignedUsers.split(",").length }}/{{
                  event.EventMaxUsers
                }}</span
              ><br />
              {{ event.EventAddress }}<br />
              {{ event.EventDateOfEvent }}
            </div>
          </router-link>
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
import axios from "axios";
import Modal from "./AddNewEventModal.vue";

export default {
  name: "MainPage",
  components: {
    Modal,
  },
  data() {
    return {
      events: [],
      ids: [1,5],
      PhotoPath: "http://127.0.0.1:8000/Photos/",
      format: ".jpg",
      user: "null",
    };
  },
  methods: {
    replaceByDefault(e) { 
      e.target.src = "http://127.0.0.1:8000/Photos/NoPhoto.jpg";
    },
    getEvents() {
      axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response) => {
        let abc = response.data[0].UserFavorites.split(",")
        this.ids = abc.filter(function (e) {return e !== ""});
        for (const item in this.ids){       
                axios.get("http://127.0.0.1:8000/events/" + this.ids[item])
                .then((response) => {
                    this.events.push(response.data[0])
                    });
                }
        })

        },
    },
  mounted: function () {
    this.user = localStorage.getItem("user-storage").replace(/['"]+/g, "");
    this.getEvents();
  },
};
</script>

<style>
.mainpage{
  text-align: left;
}

.event-list {
  list-style-type: none;
  display: inline-block;
  /*width: 100;*/
  /*background-color: thistle;*/
}

.event-name {
  font-weight: bold;
  font-size: 20px;
}

.event-image {
  aspect-ratio: calc(16 / 8);
  float: center;
  border-radius: 5px;
  width: 100%;
  min-height: 100px;
  outline: 3px solid #42b983;
  margin-bottom: 7px;
  object-fit: cover;
}

.box:hover {
  transform: scale(1.07);
  cursor: pointer;
}

.box {
  aspect-ratio: 69%;
  background-color: #dceeea;
  border-radius: 5px;
  width: 18vw;
  min-width: 225px !important;
  margin: 7px;
  padding: 12px;
  line-height: 20px;
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
  margin-top: 1.7rem;
  text-align: center;  
}

.filters{
  background-color: #dceeea;
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
  outline: 3px solid #42b983;
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
}

.scrollmenu {
  scrollbar-color: #42b983 #dceeea;
}

.filters.friends-btn{
  height: 30px;
  line-height: 0.1;
  margin-top: 0.7vw;
}

.filters.friends-btn:focus{
  background-color: transparent;
}

</style>