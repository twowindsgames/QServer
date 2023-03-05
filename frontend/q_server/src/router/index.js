import { createRouter, createWebHistory } from 'vue-router'
import HomeView from "@/views/HomeView";
import HomeView1 from "@/views/HomeView1";



const routes = [
  {
    path: '/storage/',
    name: 'HomeView',
    components: {
      default: HomeView,
      }
    },
     {
    path: '/storage/mix',
    name: 'HomeView1',
    components: {
      default: HomeView1,
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
