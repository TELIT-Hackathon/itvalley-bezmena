import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainPage.vue'
import DetailEvent from '../views/DetailEvent.vue'
import Profile from '../views/Profile.vue'
import Registration from '../views/Registration.vue'
import SignUp from '../views/SignUp.vue'
import WelcomePage from '../views/WelcomePage.vue'
import FavoriteEvents from '../views/FavoriteEvents.vue'

const routes = [
  {
    path: '/',
    name: 'WelcomePage',
    component: WelcomePage
  },
  {
    path: '/mainpage',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/detailevent/:id',
    name: 'DetailEvent',
    component: DetailEvent
  },
  {
    path: '/profile/:name',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/registration',
    name: 'Registration',
    component: Registration
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/favorite',
    name: 'FavoriteEvents',
    component: FavoriteEvents
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
