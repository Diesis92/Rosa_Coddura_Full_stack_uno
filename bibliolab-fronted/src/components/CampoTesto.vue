<script setup>

const props = defineProps({
  modelValue: { type: String, default: '' },
  label: { type: String, default: '' },
  placeholder: { type: String, default: '' },
  error: { type: String, default: '' },
  required: { type: Boolean, default: false }
})

const emit = defineEmits(['update:modelValue'])

function onInput(event) {
  emit('update:modelValue', event.target.value)
}
</script>

<template>
  <div class="campo-testo">
    <label v-if="props.label">
      {{ props.label }}
      <span v-if="props.required" class="required">*</span>
    </label>

    <input
      type="text"
      :value="props.modelValue"
      :placeholder="props.placeholder"
      :required="props.required"
      @input="onInput"
      :class="{ errore: props.error }"
    />

    <p v-if="props.error" class="messaggio-errore">
      {{ props.error }}
    </p>
  </div>
</template>

.campo-testo {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
  font-family: Arial, sans-serif;
}

/* LABEL */
.campo-testo label {
  font-weight: 600;
  margin-bottom: 0.3rem;
  color: #333;
}

/* ASTERISCO REQUIRED */
.required {
  color: #e53935;
  margin-left: 4px;
}

/* INPUT BASE */
.campo-testo input {
  padding: 10px 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  transition: all 0.2s ease;
  outline: none;
}

/* HOVER */
.campo-testo input:hover {
  border-color: #999;
}

/* FOCUS */
.campo-testo input:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}

/* 🔴 STATO ERRORE INPUT */
.campo-testo input.errore {
  border-color: #e53935;
  background-color: #fff5f5;
}

/* 🔴 MESSAGGIO ERRORE */
.messaggio-errore {
  margin-top: 0.3rem;
  font-size: 12px;
  color: #e53935;
}
