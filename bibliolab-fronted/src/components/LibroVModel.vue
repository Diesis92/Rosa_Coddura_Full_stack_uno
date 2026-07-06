<script setup>
/* global defineProps, defineEmits */

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
  <!-- Input custom (componente riutilizzabile con v-model, label, placeholder ed errori) -->
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

    <p v-if="props.error" class="errore-msg">
      {{ props.error }}
    </p>

  </div>
</template>

<style scoped>
.campo-testo {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
}

.campo-testo label {
  font-weight: 600;
  margin-bottom: 0.3rem;
}

.required {
  color: red;
  margin-left: 4px;
}

.campo-testo input {
  padding: 8px 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  outline: none;
  transition: 0.2s;
}

.campo-testo input:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
}

.campo-testo input.errore {
  border-color: #e53935;
  background-color: #fff5f5;
}

.errore-msg {
  color: #e53935;
  font-size: 12px;
  margin-top: 4px;
}
</style>
