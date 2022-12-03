<template>
  <div class="modal-backdrop" style="z-index:1000">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">{{ $t("AddNewEventModal.CreateEvent") }}</slot>
        <button type="button" class="btn-close" @click="closeModal">x</button>
      </header>

      <section class="modal-body">
        <div>
          <form @submit.prevent="createEvent">
            <label>{{ $t("AddNewEventModal.Name") }}</label>
            <input type="text" v-model="EventName" required />

            <label>{{ $t("AddNewEventModal.Address") }}</label>
            <input type="text" v-model="EventAddress" required />

            <label>{{ $t("AddNewEventModal.Date") }}</label>
            <input type="date" v-model="EventDateOfEvent" required />

            <label>{{ $t("AddNewEventModal.Description") }}</label>
            <input type="text" v-model="EventDescription" required />

            <label>{{ $t("AddNewEventModal.Capacity") }}</label>
            <input type="number" v-model="EventMaxUsers" required />

            <label>{{ $t("AddNewEventModal.Category") }}</label><br>
            <input type="radio" name="labels" value="sport" v-model="picked">{{ $t("AddNewEventModal.CategorySport") }}<br>
            <input type="radio" name="labels" value="entertainment" v-model="picked">{{ $t("AddNewEventModal.CategoryEntertainment") }}<br>
            <input type="radio" name="labels" value="music" v-model="picked">{{ $t("AddNewEventModal.CategoryMusic") }}<br>
            <input type="radio" name="labels" value="travelling" v-model="picked">{{ $t("AddNewEventModal.CategoryTravelling") }}<br>
            <input type="radio" name="labels" value="food" v-model="picked">{{ $t("AddNewEventModal.CategoryFood") }}<br>
            <input type="radio" name="labels" value="education" v-model="picked">{{ $t("AddNewEventModal.CategoryEducation") }}<br>
            <input type="radio" name="labels" value="other" v-model="picked">{{ $t("AddNewEventModal.CategoryOther") }}<br>
            
            <label>{{ $t("AddNewEventModal.Photo") }}</label>
            <input type="file" id="image" class="browse-images" v-on:change="onFileChange" required/><br>            
            <Notification messg="Nazov eventu nemoze obsahovat medzeru" format="1" v-if="this.NotifError" />
            <div class="button">
              <button class="submit" type="submit">
                {{ $t("AddNewEventModal.CreateEvent") }}
              </button>
            </div>
          </form>
        </div>
      </section>

      <footer class="modal-footer">
        <button type="button" class="btn-green" @click="closeModal">
          {{ $t("AddNewEventModal.CloseWindow") }}
        </button>
      </footer>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import Notification from "./Notification.vue";

export default {
  name: "Modal",
  components: {
    Notification,
  },
  data() {
    return {
      user: "null",
      textik: "",
      EventDateOfEvent: new Date().toISOString().substr(0, 10),
      NotifError:false
    };
  },
  methods: {
    closeModal() {
      //ZATVORENIE MODALNEHO OKNA
      this.$emit("close");
    },
    createEvent() {
      if(this.EventName.includes(" ")) {
        this.NotifError=true
        return
      }
      //console.log(this.EventAddress.match("^[a-zA-Z0-9\s,'-]*$"))
      //console.log(this.photo[0].name.match("jpg$"))

      //SUBMIT FORMULARU
      //ZISKANIE AKTUALNEHO CASU
      
      var today = new Date();
      var dd = String(today.getDate()).padStart(2, "0");
      var mm = String(today.getMonth() + 1).padStart(2, "0");
      var yyyy = today.getFullYear();
      today = yyyy + "-" + mm + "-" + dd;

      //PRIDANIE OBRAZKOV
      let formData = new FormData();
      formData.append("file", this.photo[0]);
      axios.post(
        "http://127.0.0.1:8000/events/savefile/" + this.EventName,
        formData
      );

      //POST EVENTU
      axios
        .post("http://127.0.0.1:8000/events", {
          EventName: this.EventName,
          EventAddress: this.EventAddress,
          EventDescription: this.EventDescription,
          EventOwner: this.user,
          EventDateOfCreate: today,
          EventDateOfEvent: this.EventDateOfEvent,
          EventMaxUsers: this.EventMaxUsers,
          EventSignedUsers: "",
          EventFilter: this.picked
        })
        .then((response) => {
          let abc = response.data
          axios.get("http://127.0.0.1:8000/pokus/" + this.user).then((response)=> {
                let tempUser = response.data[0].UserOwnedEvents.split(",")
                tempUser.push(abc.toString())
                axios.put("http://127.0.0.1:8000/pokus/" + this.user, {
                  UserId: response.data[0].UserId,
                  UserName: response.data[0].UserName,
                  UserAddress: response.data[0].UserAddress,
                  UserDescription: response.data[0].UserDescription,
                  UserEvents: response.data[0].UserEvents,
                  UserFavorites: response.data[0].UserFavorites,
                  UserFriends: response.data[0].UserFriends,
                  UserOwnedEvents: tempUser.toString()
                });
                //this.$router.push("/");
                //window.location.reload();
          })

        });
        this.$emit("close");

    },
    onFileChange(e) {
      //ULOZENIE ZMENY OBRAZKU
      this.photo = e.target.files;
    },
  },
  mounted: function () {
    this.user = localStorage.getItem("user-storage").replace(/['"]+/g, "");
  },
};
</script>


<style>
form {
  max-width: 600px;
  margin: 30px auto;
  background: #fff;
  text-align: left;
  padding: 20px;
  border-radius: 10px;
}

label {
  color: #aaa;
  display: inline-block;
  margin: 25px 0 15px;
  text-transform: uppercase;
}

input {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
  font-size: 0.9rem;
}

input[type="radio"] {
  margin: 0 1rem 0.5rem 1rem;
  width: auto;
  display: inline-flex;
  border-radius: 50%;
  scale: 1.4;
  accent-color: #42b983;
}

input{
  outline: none;
}

input::file-selector-button {
  font-weight: bold;
  color:#020381;
  padding: 0.5em;
  border: 0 solid #e2e8f0;
  border-radius: 1.5rem;
  background-color: #dceeea;
  padding: 0.5rem 1rem 0.5rem 1rem;
  cursor: pointer;
}

input[type="checkbox"] {
  display: inline-block;
  width: 16px;
  margin: 0 10px 0;
  position: relative;
  top: 2px;
}

.pill {
  display: inline-block;
  margin: 20px 10px 0 0;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  cursor: pointer;
  background: #eee;
}

button {
  background-color: #020381;
  border: 0 solid #e2e8f0;
  border-radius: 1.5rem;
  box-sizing: border-box;
  color: #ffffff;
  cursor: pointer;
  display: inline-block;
  font-family: "Roboto Black", Monospaced, sans-serif;
  font-size: 1.05rem;
  font-weight: 600;
  line-height: 1;
  outline: none;
  padding: 1rem 1.6rem;
  text-align: center;
  text-decoration: none #0d172a solid;
  text-decoration-thickness: auto;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

button:hover {
  background-color: #1e293b;
  color: #fff;
}

@media (min-width: 700px) {
  button {
    font-size: 1.05rem;
    padding: 1rem 2rem;
  }
}

.error {
  color: #ff0000;
  margin-top: 10px;
  font-size: 0.8em;
  font-weight: bold;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #ffffff;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
  width: 50%;
  height: 80%;
}

.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}

.modal-header {
  position: relative;
  border-bottom: 1px solid #eeeeee;
  color: #4aae9b;
  justify-content: space-between;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  flex-direction: column;
  justify-content: flex-end;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
}

.btn-close {
  position: absolute;
  top: 5px;
  right: 7px;
  border: none;
  font-size: 1.5rem;
  padding: 7px 12px;
  cursor: pointer;
  font-weight: bold;
  color: #2874FC;
  background: transparent;
}

.btn-green {
  color: white;
  background: #020381;
  border: 1px solid #020381;
  border-radius: 2px;
}
</style>
