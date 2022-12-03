<template>
  <div>
    <form @submit.prevent="registerUser">
      <label>{{ $t("Registration.Name") }}</label>
      <input type="text" v-model="UserName" required />

      <label>{{ $t("Registration.Password") }}</label>
      <input type="password" v-model="UserPassword" required />

      <label>{{ $t("Registration.Email") }}</label>
      <input type="email" v-model="UserEmail" required />

      <label>{{ $t("Registration.Address") }}</label>
      <input type="text" v-model="UserAddress" required />

      <label>{{ $t("Registration.Description") }}</label>
      <input type="text" v-model="UserDescription" required />

      <label>{{ $t("Registration.Photo") }}</label>
      <input type="file" id="image" v-on:change="onFileChange" required />

      <div>
        <input type="checkbox" v-model="terms" required />
        <label>{{ $t("Registration.Agree") }}</label>
      </div>
        <button class="submit" type="submit">
          {{ $t("Registration.Register") }}
        </button>
    </form>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "Registration",
  data() {
    return {
      events: [],
      photo: null,
    };
  },
  methods: {
    registerUser() {
      var today = new Date();
      var dd = String(today.getDate()).padStart(2, "0");
      var mm = String(today.getMonth() + 1).padStart(2, "0"); //January is 0!
      var yyyy = today.getFullYear();
      today = yyyy + "-" + mm + "-" + dd;

      let formData = new FormData();
      formData.append("file", this.photo[0]);

      axios.post(
        "http://127.0.0.1:8000/events/savefile/" + this.UserName,
        formData
      );

      axios.post("http://127.0.0.1:8000/users", {
        UserName: this.UserName,
        UserAddress: this.UserAddress,
        UserDescription: this.UserDescription,
        UserEvents: "",
        UserFavorites: "",
        UserFriends: "",
        UserOwnedEvents: "",
      });

      axios
        .post("http://127.0.0.1:8000/register", {
          UserName: this.UserName,
          UserPassword: this.UserPassword,
          UserEmail: this.UserEmail,
        })
        .then(() => {
          this.$router.push("/");
        });
    },
    onFileChange(e) {
      this.photo = e.target.files;

    },
  }
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
  top: -2px;
  cursor: pointer;
  scale: 1.5;
  accent-color: #42b983;
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