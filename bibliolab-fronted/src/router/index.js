import { createRouter, createWebHistory } from 'vue-router'

import RicercaLibri from '@/components/RicercaLibri.vue'
import NotFoundView from '@/views/NotFoundView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),

  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }

    return { top: 0 }
  },

  routes: [
    {
      path: '/',
      redirect: '/catalogo'
    },
    {
      path: '/catalogo',
      name: 'catalogo',
      component: () => import('@/views/CatalogoView.vue'), // Lazy loading
      meta: {
        title: 'Il catalogo dei libri'
      }
    },
    {
      path: '/ricerca',
      name: 'ricerca',
      component: RicercaLibri
    },

    // Catch-all 404
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: NotFoundView
    }
  ]
})

export default router
