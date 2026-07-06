<script setup>
import { ref, computed } from 'vue'

const libri = ref([
  { id: 1, titolo: 'Il Nome della Rosa', autore: 'Eco', anno: 1980, genere: 'narrativa', disponibile: true },
  { id: 2, titolo: 'Se questo è un uomo', autore: 'Levi', anno: 1947, genere: 'narrativa', disponibile: false },
  { id: 3, titolo: 'La luna e i falò', autore: 'Pavese', anno: 1950, genere: 'narrativa', disponibile: true },
  { id: 4, titolo: 'I Promessi Sposi', autore: 'Manzoni', anno: 1827, genere: 'narrativa', disponibile: true },
  { id: 5, titolo: 'Storia del mondo moderno', autore: 'Hobsbawm', anno: 1994, genere: 'storia', disponibile: true },
  { id: 6, titolo: 'Il sistema periodico', autore: 'Primo Levi', anno: 1975, genere: 'saggio', disponibile: true },
])

const filtro = ref('')
const genereSelezionato = ref('Tutti')
const soloDisponibili = ref(false)

const generi = ref(['Tutti', 'narrativa', 'storia', 'saggio'])

// 🔎 computed principale
const libriFiltratiCombinati = computed(() => {
  return libri.value.filter((libro) => {
    const matchTesto =
      libro.titolo.toLowerCase().includes(filtro.value.toLowerCase()) ||
      libro.autore.toLowerCase().includes(filtro.value.toLowerCase())

    const matchGenere =
      genereSelezionato.value === 'Tutti' ||
      libro.genere === genereSelezionato.value

    const matchDisponibile =
      !soloDisponibili.value || libro.disponibile

    return matchTesto && matchGenere && matchDisponibile
  })
})

// 📊 computed derivati
const totaleLibriFiltrati = computed(() =>
  libriFiltratiCombinati.value.length
)

const totaleDisponibili = computed(() =>
  libriFiltratiCombinati.value.filter(l => l.disponibile).length
)
</script>

<template>
  <div class="ricerca-libri">
    <h2>Ricerca Libri</h2>

    <!-- ricerca testo -->
    <input
      v-model="filtro"
      placeholder="Cerca per titolo o autore"
    />

    <!-- filtro genere -->
    <select v-model="genereSelezionato">
      <option
        v-for="genere in generi"
        :key="genere"
        :value="genere"
      >
        {{ genere }}
      </option>
    </select>

    <!-- checkbox disponibili -->
    <label>
      <input type="checkbox" v-model="soloDisponibili" />
      Solo disponibili
    </label>

    <!-- statistiche -->
    <div class="stats">
      <p>Trovati: <strong>{{ totaleLibriFiltrati }}</strong></p>
      <p>Disponibili: <strong>{{ totaleDisponibili }}</strong></p>
      <p>{{ totaleLibriFiltrati }} risultati su {{ libri.length }}</p>
    </div>

    <!-- lista -->
    <ul>
      <li
        v-for="libro in libriFiltratiCombinati"
        :key="libro.id"
      >
        <strong>{{ libro.titolo }}</strong>
        di {{ libro.autore }}
        ({{ libro.anno }})

        -
        <span v-if="libro.disponibile" class="ok">
          Disponibile
        </span>
        <span v-else class="no">
          Non disponibile
        </span>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.ricerca-libri {
  max-width: 600px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}

input,
select {
  display: block;
  margin: 10px 0;
  padding: 8px;
  width: 100%;
}

.stats {
  margin: 15px 0;
  padding: 10px;
  background: #f5f5f5;
  border-radius: 6px;
}

.ok {
  color: green;
  font-weight: bold;
}

.no {
  color: red;
  font-weight: bold;
}
</style>
