import { reactive, computed } from 'vue'

export function useForm(campiIniziali, regoleValidazione) {
  const campi = reactive({ ...campiIniziali })
  const errori = reactive({})

  // 🔥 COMPUTED: il form è valido se NON ci sono errori
  const isValid = computed(() => {
    return Object.values(errori).every(e => !e)
  })

  function validazione() {
    let valido = true

    for (const campo in regoleValidazione) {
      const valore = campi[campo]
      const regola = regoleValidazione[campo]

      const risultato = regola(valore)

      if (risultato === true) {
        errori[campo] = ''
      } else {
        errori[campo] = risultato
        valido = false
      }
    }

    return valido
  }

  function resetForm() {
    Object.assign(campi, campiIniziali)

    Object.keys(errori).forEach(key => {
      delete errori[key]
    })
  }

  return {
    campi,
    errori,
    validazione,
    resetForm,
    isValid
  }
}
