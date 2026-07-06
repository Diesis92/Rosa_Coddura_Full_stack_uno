<script setup>
import { useForm } from '../composables/useForm'

const { campi, errori, validazione, resetForm, isValid } = useForm(
  {
    titolo: '',
    autore: '',
    anno: '',
    genere: 'narrativa',
    disponibile: true,
    isbn: '',
  },
  {
    titolo: v => v.length > 0 || 'Il titolo è obbligatorio',
    autore: v => v.length > 0 || "L'autore è obbligatorio",
    anno: v => v.length > 0 || "L'anno è obbligatorio",
    genere: v => v.length > 0 || 'Il genere è obbligatorio',
    isbn: v =>
      !v || /^97[89]/.test(v) || "L'ISBN deve iniziare con 978 o 979",
  }
)

async function salvaLibro() {
  const valido = validazione()
  if (!valido) return

  await fetch('http://localhost:3000/libri', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(campi)
  })

  resetForm()
}
</script>

<template>
  <form @submit.prevent="salvaLibro">

    <div>
      <label>Titolo*</label>
      <input v-model="campi.titolo" />
      <p v-if="errori.titolo" class="errore">{{ errori.titolo }}</p>
    </div>

    <div>
      <label>Autore*</label>
      <input v-model="campi.autore" />
      <p v-if="errori.autore" class="errore">{{ errori.autore }}</p>
    </div>

    <div>
      <label>Anno*</label>
      <input v-model="campi.anno" />
      <p v-if="errori.anno" class="errore">{{ errori.anno }}</p>
    </div>

    <div>
      <label>Genere*</label>
      <input v-model="campi.genere" />
      <p v-if="errori.genere" class="errore">{{ errori.genere }}</p>
    </div>

    <div>
      <label>ISBN</label>
      <input v-model="campi.isbn" />
      <p v-if="errori.isbn" class="errore">{{ errori.isbn }}</p>
    </div>

    <div>
      <label>
        <input type="checkbox" v-model="campi.disponibile" />
        Disponibile
      </label>
    </div>

    <button type="submit" :disabled="!isValid">
      Salva libro
    </button>

    <button type="button" @click="resetForm">
      Annulla
    </button>

  </form>
</template>
