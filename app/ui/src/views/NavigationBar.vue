<template>
  <div class="nav">
    <router-link to="/mainpage"
      ><img src="../images/BroFinder-Logo.jpg" class="logo-top-left"
    /></router-link>

    <span v-if="this.user != null && this.user != 'null'">
      <router-link :to="'/profile/' + this.user"
        >{{ this.user }}
        <img
          :src="PhotoPath + this.user + format"
          class="profile-picture-small"
          @error="replaceByDefault"
        />
      </router-link>
    </span>

    <LanguageSwitcher />

    <button
      v-if="this.user != null && this.user != 'null'"
      type="button"
      class="btn"
      @click="logoutUser" style="margin-left: 5px"
    >
      {{ $t("NavigationBar.Logout") }}
    </button>
    <button
      v-if="
        !(this.user != null && this.user != 'null') &&
        this.$route.path != '/signup' && this.$route.path != '/'
      "
      type="button"
      class="btn"
      @click="redirectSignUpPage" style="margin-left: 5px"
    >
      {{ $t("NavigationBar.SignUp") }}
    </button>
    <button
      v-if="
        !(this.user != null && this.user != 'null') &&
        this.$route.path != '/registration' && this.$route.path != '/'
      "
      type="button"
      class="btn"
      @click="redirectRegistrationPage" style="margin-left: 5px"
    >
      {{ $t("NavigationBar.Registration") }}
    </button>
  </div>
</template>

<style>
.nav {
  padding: 10px 3% 0 3%;
  text-align: right !important;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #020381;
}

.logo-top-left {
  float: left;
  width: calc(150px + 4.5vw);
  height: auto;
  margin-top: 20px;
}

.profile-picture-small {
  aspect-ratio: 1;
  border-radius: 50%;
  height: 2.65rem;
  width: 2.65rem;
  outline: 2px solid #020381;
  object-fit: cover;
  margin: 0 10px -14px 10px;
}
</style>

<script>
import axios from "axios";
import LanguageSwitcher from "./LanguageSwitcher.vue";

export default {
  name: "NavigationBar",
  components: {
    LanguageSwitcher,
  },
  data() {
    return {
      user: "null",
      PhotoPath: "http://127.0.0.1:8000/Photos/",
      format: ".jpg",
    };
  },
  methods: {
    replaceByDefault(e) {
      e.target.src = "http://127.0.0.1:8000/Photos/NoPhoto.jpg";
    },
    logoutUser() {
      axios.post("http://127.0.0.1:8000/logout").then(() => {
        localStorage.setItem("user-storage", "null");
        this.user = "null";
      });
    },
    redirectSignUpPage() {
      this.$router.push("signup");
    },
    redirectRegistrationPage() {
      this.$router.push("registration");
    },
  },
  mounted: function () {
    this.user = localStorage.getItem("user-storage").replace(/['"]+/g, "");
  },
};
</script>
