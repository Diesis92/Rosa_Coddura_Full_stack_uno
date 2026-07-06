import { ref } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)
  const caricamento = ref(true)

  async function carica() {
    caricamento.value = true
    error.value = null

    try {
      const res = await fetch(url)

      if (!res.ok) {
        throw new Error(`Errore HTTP! status: ${res.status}`)
      }

      data.value = await res.json()
    } catch (err) {
      error.value = err.message
    } finally {
      caricamento.value = false
    }
  }

  // 👇 il composable deve restituire queste refs
  return { data, error, caricamento, carica }
}
