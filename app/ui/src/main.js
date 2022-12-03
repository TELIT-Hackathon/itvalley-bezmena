import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import i18n from './i18n'
import VueAwesomePaginate from "vue-awesome-paginate";
import "vue-awesome-paginate/dist/style.css";

createApp(App).use(i18n).use(router).use(VueAwesomePaginate).mount('#app')
