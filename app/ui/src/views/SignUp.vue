<template>
  <div>
    <Notification
      messg="Zle meno alebo heslo"
      format="1"
      v-if="this.notification"
    />

    <form @submit.prevent="loginUser">
      <label>{{ $t("SignUp.Name") }}</label>
      <input type="text" v-model="UserName" required />

      <label>{{ $t("SignUp.Password") }}</label>
      <input type="password" v-model="UserPassword" required />

      <div class="button">
        <button class="submit" type="submit" style="margin-top: 1rem">{{ $t("SignUp.SignUp") }}</button>
      </div>
    </form>
  </div>
</template>



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


<style scoped>
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

input,
select {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: bordre-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
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

.error {
  color: #ff0000;
  margin-top: 10px;
  font-size: 0.8em;
  font-weight: bold;
}
</style>