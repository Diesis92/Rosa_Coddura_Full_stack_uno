<script setup>
import { onMounted } from 'vue'
import { useFetch } from '@/composables/useFetchL.js'

const {
  data: libri,
  error,
  caricamento,
  carica,
} = useFetch('http://localhost:3000/libri')

onMounted(() => {
  carica()
})
</script>

<template>
  <div>

    <!-- LOADING -->
    <p v-if="caricamento">Caricamento in corso...</p>

    <!-- ERROR -->
    <p v-else-if="error">{{ error }}</p>

    <!-- DATA -->
    <ul v-else>
      <li v-for="libro in libri" :key="libro.id">
        {{ libro.titolo }} - {{ libro.autore }}
      </li>
    </ul>

  </div>
</template>
