<script setup>
const props = defineProps({
  id: { type: Number, required: true },
  titolo: { type: String, required: true },
  autore: { type: String, required: true },
  anno: { type: Number, required: true },
  genere: { type: String, required: true },
  disponibile: { type: Boolean, required: true },
  isbn: { type: String, required: true }
})

const emit = defineEmits([
  'elimina-libro',
  'cambia-stato-disponibilita',
  'modifica-libro',
  'evidenzia'
])

function onElimina() {
  if (confirm(`Sei sicuro di voler eliminare il libro "${props.titolo}"?`)) {
    emit('elimina-libro', props.id)
  }
}

function onCambiaStatoDisponibilita() {
  emit('cambia-stato-disponibilita', {
    id: props.id,
    disponibile: props.disponibile
  })
}

function evidenzia() {
  emit('evidenzia', props.id)
}
</script>

<template>
  <div class="libro">

    <h3>{{ titolo }}</h3>

    <p>Autore: {{ autore }}</p>
    <p>Anno: {{ anno }}</p>
    <p>Genere: {{ genere }}</p>
    <p>Disponibile: {{ disponibile ? 'Sì' : 'No' }}</p>

    <!-- emit originali -->
    <button class="btn" @click="onElimina">
      Elimina
    </button>

    <button class="btn" @click="onCambiaStatoDisponibilita">
      {{ disponibile ? 'Segna come non disponibile' : 'Segna come disponibile' }}
    </button>

    <!-- ⭐ nuovo emit (aggiunto) -->
    <button class="star-btn" @click="evidenzia">
      ⭐ In evidenza
    </button>

  </div>
</template>

<style scoped>
.libro {
  border: 1px solid #ddd;
  padding: 16px;
  margin-bottom: 12px;
  border-radius: 8px;
}

.btn {
  margin-right: 8px;
  padding: 6px 10px;
  border: 1px solid #ccc;
  background: white;
  cursor: pointer;
}

.btn:hover {
  background: #f5f5f5;
}

.star-btn {
  padding: 6px 10px;
  border: 1px solid #ccc;
  background: transparent;
  cursor: pointer;
  border-radius: 6px;
  margin-top: 8px;
}

.star-btn:hover {
  background: #fff3b0;
}
</style>
