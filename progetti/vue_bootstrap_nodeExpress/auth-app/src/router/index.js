// Importiamo gli strumenti necessari da Vue Router
import { createRouter, createWebHistory } from 'vue-router'

// Creiamo il router dell'applicazione
const router = createRouter({

  // Permette di utilizzare URL normali come:
  // http://localhost:5173/login
  history: createWebHistory(import.meta.env.BASE_URL),

  // Qui definiamo le rotte (pagine) del frontend
  routes: [

    {
      // URL della pagina
      path: '/login',

      // Nome interno della rotta
      name: 'login',

      // Componente da mostrare quando visitiamo /login
      //
      // Usiamo il lazy loading:
      // LoginView.vue viene caricato solo quando l'utente
      // visita effettivamente la pagina /login
      component: () => import('../views/LoginView.vue'),
    },

  ],
})

// Esportiamo il router per poterlo utilizzare in main.js
export default router
