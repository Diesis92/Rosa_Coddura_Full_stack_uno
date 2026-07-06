<script setup>
/*
  COMPONENTE CARD (FIGLIO)
  ------------------------
  Componente riutilizzabile che riceve dati tramite props
  e permette contenuto dinamico tramite slot.
*/

defineProps({
  id: { type: Number, required: true },
  titolo: { type: String, required: true },
  autore: { type: String, required: true },
  anno: { type: Number, required: true },
  genere: { type: String, required: true },
  disponibile: { type: Boolean, required: true },
})
</script>

<template>
  <div class="card">

    <!-- Titolo principale della card -->
    <h3 class="card-titolo">{{ titolo }}</h3>

    <!-- Slot: contenuto personalizzabile dal componente padre -->
    <div class="card-body">
      <slot>
        <!-- Contenuto di default se lo slot è vuoto -->
        <p>Nessun contenuto disponibile</p>
      </slot>
    </div>

    <!-- Dati del libro mostrati sempre -->
    <div class="card-footer">
      <p><strong>Autore:</strong> {{ autore }}</p>
      <p><strong>Anno:</strong> {{ anno }}</p>
      <p><strong>Genere:</strong> {{ genere }}</p>

      <p>
        <strong>Disponibile:</strong>
        <span :class="{ yes: disponibile, no: !disponibile }">
          {{ disponibile ? 'Sì' : 'No' }}
        </span>
      </p>
    </div>

  </div>
</template>

<template>
  <div class="layout">

    <header class="layout-header">
      <slot name="header">
        <h1>Benvenuto nella Libreria</h1>
      </slot>
    </header>

    <aside class="layout-sidebar">
      <slot name="sidebar">
        <p>Menu laterale</p>
      </slot>
    </aside>

    <main class="layout-main">
      <slot name="main">
        <p>Contenuto principale</p>
      </slot>
    </main>

    <footer class="layout-footer">
      <slot name="footer">
        <p>Footer di default</p>
      </slot>
    </footer>

  </div>
</template>

//naming e composables es. useFetch.js, useForm.js, useAuth.js, useCart.js, useModal.js, useTheme.js, useLocalStorage.js, useSessionStorage.js, useDebounce.js, useThrottle.js, useInfiniteScroll.js, useIntersectionObserver.js
// si trovano nella cartella src/composables e contengono logica riutilizzabile per componenti Vue.
// stato indipendente, gestione di API, gestione di form, autenticazione, carrello, modali, temi, localStorage/sessionStorage, debounce/throttle, infinite scroll e intersection observer.
// separazione della responsabilità della logica di business dalla presentazione, migliorando la manutenibilità e la riusabilità del codice.
