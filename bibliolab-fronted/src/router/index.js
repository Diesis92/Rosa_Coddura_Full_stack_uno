import { createRouter, createWebHistory } from 'vue-router'

import CatalogoView from '@/views/CatalogoView.vue'
import RicercaLibri from '@/components/RicercaLibri.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/catalogo'
    },
    {
      path: '/catalogo',
      name: 'catalogo',
      component: CatalogoView
    },
    {
      path: '/ricerca',
      name: 'ricerca',
      component: RicercaLibri
    }
  ]
})

export default router
