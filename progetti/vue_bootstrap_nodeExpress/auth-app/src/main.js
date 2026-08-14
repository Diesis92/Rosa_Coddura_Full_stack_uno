// CSS globale dell'applicazione
import './assets/main.css'

// CSS di Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'

// JavaScript di Bootstrap
import 'bootstrap'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Creiamo l'applicazione Vue partendo da App.vue
const app = createApp(App)

// Aggiungiamo Vue Router all'applicazione
app.use(router)

// Montiamo l'applicazione nell'elemento #app di index.html
app.mount('#app')
