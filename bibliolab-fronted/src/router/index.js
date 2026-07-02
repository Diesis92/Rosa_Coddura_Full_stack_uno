import { createRouter, createWebHistory } from 'vue-router'

import RicercaLibri from '../components/RicercaLibri.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ricerca',
      name: 'ricerca',
      component: RicercaLibri,
    },
  ],
})

export default router
