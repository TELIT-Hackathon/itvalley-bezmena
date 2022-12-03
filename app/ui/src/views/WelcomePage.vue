<template>
  <div class="welcomepage">
  <div>
    <Notification
      messg="Zle meno alebo heslo"
      format="1"
      v-if="this.notification"
    />

    <div class="welcome-box">
      <div>
      <router-link to="/mainpage"><img src="../images/event-tree-no-white.jpg" class="tree"></router-link>
      
      </div>

      <div class="login-register">
        <div style="padding: 0 20px 0 20px">
            {{ $t("WelcomePage.MainText") }}
        </div>
        <form @submit.prevent="loginUser" style="margin-top: 10px">
          <label>{{ $t("WelcomePage.Name") }}</label>
          <input type="text" v-model="UserName" required />

          <label>{{ $t("WelcomePage.Password") }}</label>
          <input type="password" v-model="UserPassword" required />
          
          <div style="left: 45%; position: absolute">
          <button class="submit" type="submit" style="margin-top: 1rem; ">{{ $t("WelcomePage.SignUp") }}</button>
          </div>          
        </form>
        <div style="margin-top: 3.5rem; text-align: center;">{{ $t("WelcomePage.NoAcc") }}
          <router-link :to="'/registration'" style="color: #020381">{{ $t("WelcomePage.CreateAcc") }}</router-link></div>
      </div>
    </div>

  </div>
</div>
</template>

<style>
.welcomepage{
  margin: 0 3% 0 3%;
  padding-right: 3%;  
}

.welcome-box{
  border-radius: 0.3rem;
  margin: 0 0 2rem 0;
  border-radius: 0.3rem;
  width: 94vw;
  height: auto;
  line-height: 1.2rem !important;
  overflow: hidden !important;
  justify-content: center;
}
.tree{
  width: calc(100px + 27%);
  height: auto;
  float:left;
  margin: 5vw 0 3vw 10vw;
}

.login-register{
  width: calc(35vw);
  aspect-ratio: 25%;
  min-width: 300px;
  margin: 7vw 11vw 10vw 0;
  padding-left: 2vw;
  position: relative;
  float: right;
  border-left: 2px solid #8f8f8f;
}

.tree-btn{
  position: absolute;
  outline: none;
  left: calc( 1rem + 24vw);
  top: calc( 7rem + 17vw);
  font-size: calc(9px + 0.5vw);
  padding: 1vw 2vw;  
}

</style>

<script>
import axios from "axios";
import Notification from "./Notification.vue";

export default {
  name: "SignUp",
  components: {
    Notification,
  },
  data() {
    return {
      events: [],
      notification: false,
    };
  },
  methods: {
    loginUser() {
      axios
        .post("http://127.0.0.1:8000/login", {
          UserName: this.UserName,
          UserPassword: this.UserPassword,
        })
        .then((response) => {
          if (response.data != "Chyba") {
            localStorage.setItem("user-storage", JSON.stringify(this.UserName));
            this.$router.push("/");
            window.location.reload();
          } else {
            this.UserName = "";
            this.UserPassword = "";
            this.notification = true;
          }
        });
    },
  },
};
</script>