<script setup>
import { ref, onMounted } from 'vue'
import LibroCard from '@/components/LibroCard.vue'

const API_URL = 'http://localhost:3000'

const libri = ref([])

/*
  ascolta l'evento @evidenzia e aggiungi l'id ad un array idInEvidenza. = ref([])

  gestisci il toggle: se l'id è già presente, rimuovilo, altrimenti aggiungilo.

  passa al figlio la prop booleana:
  :inEvidenza="idInEvidenza.includes(libro.id)"
*/

const idInEvidenza = ref([])

// 🔥 LOAD LIBRI DAL BACKEND
onMounted(async () => {
  const res = await fetch(`${API_URL}/libri`)
  libri.value = await res.json()

  const storedIds = localStorage.getItem('idInEvidenza')
  if (storedIds) {
    idInEvidenza.value = JSON.parse(storedIds)
  }
})

// ⭐ TOGGLE EVIDENZA
function evidenzia(id) {
  const index = idInEvidenza.value.indexOf(id)

  if (index > -1) {
    idInEvidenza.value.splice(index, 1)
  } else {
    idInEvidenza.value.push(id)
  }

  localStorage.setItem(
    'idInEvidenza',
    JSON.stringify(idInEvidenza.value)
  )
}

// ❌ DELETE LIBRO (BACKEND)
function eliminaLibro(id) {
  libri.value = libri.value.filter(l => l.id !== id)

  fetch(`${API_URL}/libri/${id}`, {
    method: 'DELETE'
  })
}

// 🔄 PATCH DISPONIBILITÀ (BACKEND)
function cambiaStatoDisponibilita({ id }) {
  const libro = libri.value.find(l => l.id === id)
  if (!libro) return

  libro.disponibile = !libro.disponibile

  fetch(`${API_URL}/libri/${id}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      disponibile: libro.disponibile
    })
  })
}
</script>

<template>
  <div class="catalogo">
    <h2>Catalogo dei Libri</h2>

    <div class="libri">
      <LibroCard
        v-for="libro in libri"
        :key="libro.id"
        v-bind="libro"
        :inEvidenza="idInEvidenza.includes(libro.id)"
        @elimina-libro="eliminaLibro"
        @cambia-stato-disponibilita="cambiaStatoDisponibilita"
        @evidenzia="evidenzia"
      />

      <!-- ⭐ LISTA EVIDENZIATI -->
      <div class="evidenziati">
        <h3>Libri in evidenza</h3>

        <div v-for="libro in libri" :key="'star-' + libro.id">
          <span v-if="idInEvidenza.includes(libro.id)">
            ⭐ {{ libro.titolo }}
          </span>
        </div>
      </div>

    </div>
  </div>
</template>
