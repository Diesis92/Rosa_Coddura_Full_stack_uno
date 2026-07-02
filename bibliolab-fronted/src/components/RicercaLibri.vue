<script setup>
import { ref, computed } from 'vue'
//esercizio: creare un array di libri reattivo con ref() e un filtro di ricerca reattivo con ref(), e input di ricerca testuale con v-model. Creare un computed che filtra i libri in base al filtro di ricerca e un altro computed che conta quanti libri sono disponibili (disponibile === true). Mostrare il numero di libri trovati e il numero di libri disponibili.
const libri = ref([
  // Array reattivo: ogni modifica aggiorna automaticamente il DOM
  {
    id: 1,
    titolo: 'Il Nome della Rosa',
    autore: 'Eco',
    anno: 1980,
    genere: 'narrativa',
    disponibile: true,
  },
  {
    id: 2,
    titolo: 'Se questo è un uomo',
    autore: 'Levi',
    anno: 1947,
    genere: 'narrativa',
    disponibile: false,
  },
  {
    id: 3,
    titolo: 'La luna e i falò',
    autore: 'Pavese',
    anno: 1950,
    genere: 'narrativa',
    disponibile: true,
  },
  {
    id: 4,
    titolo: 'I Promessi Sposi',
    autore: 'Manzoni',
    anno: 1827,
    genere: 'narrativa',
    disponibile: true,
  },
  {
    id: 5,
    titolo: 'Storia del mondo moderno',
    autore: 'Eric Hobsbawm',
    anno: 1994,
    genere: 'storia',
    disponibile: true,
  },
  {
    id: 6,
    titolo: 'Il sistema periodico',
    autore: 'Primo Levi',
    anno: 1975,
    genere: 'saggio',
    disponibile: true,
  },
])
// Select per filtrare per genere con opzione "Tutti" per azzerare il filtro
const filtro = ref('') // stringa reattiva per il filtro di ricerca
const genereSelezionato = ref('Tutti') // stringa reattiva per il filtro per genere
const generi = ref(['Tutti', 'narrativa', 'storia', 'saggio'])
//Checkbox "Solo disponibili" che esclude i libri non disp
const soloDisponibili = ref(false) // booleano reattivo per il filtro "Solo disponibili", si parte dal falso perché vogliamo mostrare tutti i libri di default, anche quelli non disponibili
// computed: calcola la lista filtrata dei libri in base al filtro di ricerca
// const libriFiltrati = computed(() => {
//   return libri.value.filter((libro) => {
//     const matchTesto =
//       libro.titolo.toLowerCase().includes(filtro.value.toLowerCase()) ||
//       libro.autore.toLowerCase().includes(filtro.value.toLowerCase())

//     const matchGenere =
//     //Mostra tutti i libri se ho scelto ‘Tutti’, altrimenti mostra solo quelli del genere selezionato
//       genereSelezionato.value === 'Tutti' || libro.genere === genereSelezionato.value
//     //Se NON ho cliccato ‘solo disponibili’, mostra tutto.Se invece l’ho cliccato, mostra solo quelli disponibili
//     const matchDisponibile = !soloDisponibili.value || libro.disponibile

//     return matchTesto && matchGenere && matchDisponibile
//   })
// })

//secondo computed: filtra solo i libri disponibili === true
const totaleLibriFiltrati = computed(() =>
  libriFiltratiCombinati.value.length
)

//terzo computed: conta quanti libri sono filtrati
const totaleDisponibili = computed(() =>
  libriFiltratiCombinati.value.filter(l => l.disponibile).length // Conta i libri disponibili
)

//ho usato 3 filtri: filtro di ricerca testuale, filtro per genere e filtro per disponibilità. Tutti e 3 i filtri sono combinati nel computed libriFiltrati.
//computed combinato: filtra i libri in base a tutti e 3 i filtri
const libriFiltratiCombinati = computed(() => {
  return libri.value.filter((libro) => {
    const matchTesto =
      libro.titolo.toLowerCase().includes(filtro.value.toLowerCase()) ||
      libro.autore.toLowerCase().includes(filtro.value.toLowerCase())

    const matchGenere =
      genereSelezionato.value === 'Tutti' || // Mostra tutti i libri se ho scelto ‘Tutti’, altrimenti mostra solo quelli del genere selezionato
      libro.genere === genereSelezionato.value

    const matchDisponibile =
      !soloDisponibili.value || libro.disponibile // Se NON ho cliccato ‘solo disponibili’, mostra tutto. Se invece l’ho cliccato, mostra solo quelli disponibili

    return matchTesto && matchGenere && matchDisponibile // Tutti e 3 i filtri devono essere soddisfatti per mostrare il libro
  })
})

//Conteggio Mostra: {{ libriFiltrati.length }} libri trovati su {{ libri.length }}

</script>

<template>
  <h2>Ricerca Libri</h2>
  <input v-model="filtro" placeholder="Cerca per titolo o autore" />
  <select v-model="genereSelezionato">
  <!--:key vuol dire che ogni opzione ha un identificatore unico -->
    <option v-for="genere in generi" :key="genere" :value="genere">{{ genere }}</option>
  </select>
  <p>Filtra per genere: {{ genereSelezionato }}</p>
  <p>Trovati: {{ totaleLibriFiltrati }} || Disponibili: {{ totaleDisponibili }}</p>
  <p>{{ totaleLibriFiltrati }} risultati su {{ libri.length }}</p>
  <label>
    <input type="checkbox" v-model="soloDisponibili" />
    Solo disponibili
  </label>
  <ul>
    <li v-for="libro in libriFiltratiCombinati" :key="libro.id">
      {{ libro.titolo }} di {{ libro.autore }} ({{ libro.anno }}) -
      <span v-if="libro.disponibile">Disponibile</span>
      <span v-else>Non disponibile</span>
    </li>
  </ul>
</template>
