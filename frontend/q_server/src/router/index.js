import { createRouter, createWebHistory } from 'vue-router'
import HomeView from "@/views/HomeView";



const routes = [
  {
    path: '/storage/',
    name: 'HomeView',
    components: {
      default: HomeView,
      }
    },
    {
     path: '/',
     redirect: '/storage/'
    }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
