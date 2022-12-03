<template>
  <NavigationBar />
  <router-view/>
  <Footer />
</template>

<style>
#app {
  font-family: Avenir, Lato, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  display: block;
  background-color: white;
  margin-bottom: 100px;
}

a:link {
  text-decoration: none;
  color: #2c3e50;
  outline: none;
}

a:visited {
  text-decoration: none;
  color: #2c3e50;
}

a:active {
  text-decoration: none;
}
</style>


<script>
import NavigationBar from './views/NavigationBar.vue';
import Footer from './views/Footer.vue';

export default {
name: 'App',
    components: {
        NavigationBar,
        Footer
    }
}
</script>