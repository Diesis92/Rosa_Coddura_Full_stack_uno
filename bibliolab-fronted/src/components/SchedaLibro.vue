/*


Esercizio 3 - Scheda libro BiblioLab (1 ora)

Crea il componente src/components/SchedaLibro.vue che simula il form di inserimento reale di BiblioLab. Questo è il componente più complesso dell'unità.

Campi del form (usa reactive())

titolo - input text

autore-input text

isbn-input text (stringa)

anno-input number

genere-select (narrativa, saggistica, tecnico)

disponibile - checkbox booleano

Funzionalità richieste

Anteprima in tempo reale: "Libro: [titolo] di [autore] ([anno])"

Pulsante Salva disabilitato se titolo o autore sono vuoti

Al click su Salva: console.log() dei dati + alert di conferma

Gestisci il submit con @submit.prevent

Questo componente sarà il punto di partenza per il form reale di BiblioLab che collegheremo all'API Django nelle prossime unità.



*/

<script setup>
import { reactive } from 'vue'

// reactive() per il form: tutte le proprietà in un unico oggetto reattivo
const nuovoLibro = reactive({ //NextTick promise per problemi di rendering legate a troppe lavorazioni. Usare anche computed
  titolo: '',        // campo obbligatorio
  autore: '',         // campo obbligatorio
  isbn: '',           // stringa
  anno: '',           // stringa — type="number" nel template lo converte
  genere: 'narrativa', // valore di default per la select
  disponibile: true   // checkbox — default: spuntato
})

//computed


function salva() {
  console.log('Dati da salvare:', nuovoLibro)
  alert(`Libro "${nuovoLibro.titolo}" salvato con successo!`)
  // invieremo questi dati all'API Django con fetch()
}
</script>

<template>
  <!-- @submit.prevent: intercetta il submit del form -->
  <!-- .prevent blocca il ricaricamento della pagina (preventDefault) -->
  <form @submit.prevent="salva">

    <!-- v-model = :value + @input in una sola direttiva -->
    <!-- aggiorna nuovoLibro.titolo ad ogni tasto premuto -->
    <input v-model="nuovoLibro.titolo" placeholder="Titolo" />
    <input v-model="nuovoLibro.autore" placeholder="Autore" />
    <input v-model="nuovoLibro.isbn" placeholder="ISBN" />
    <input v-model="nuovoLibro.anno" placeholder="Anno" type="number" />

    <!-- v-model su select: aggiorna nuovoLibro.genere al cambio opzione -->
    <select v-model="nuovoLibro.genere">
      <option value="narrativa">Narrativa</option>
      <option value="saggistica">Saggistica</option>
      <option value="tecnico">Tecnico</option>
    </select>

    <!-- v-model su checkbox: lega true/false alla variabile booleana -->
    <input type="checkbox" v-model="nuovoLibro.disponibile" />
    <label>Disponibile</label>

    <!-- :disabled diventa true (bottone bloccato) se titolo o autore sono vuoti -->
    <button type="submit" :disabled="!nuovoLibro.titolo || !nuovoLibro.autore">
      Salva Libro
    </button>
  </form>

  <!-- v-if: mostra l'anteprima solo se almeno titolo o autore sono stati inseriti -->
  <!-- anteprima in tempo reale: si aggiorna ad ogni tasto -->
  <p v-if="nuovoLibro.titolo || nuovoLibro.autore">
    Libro: {{ nuovoLibro.titolo }} di {{ nuovoLibro.autore }} ({{ nuovoLibro.anno }})
  </p>
</template>
