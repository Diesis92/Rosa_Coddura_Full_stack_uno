"""
chatbot.py — Chatbot RAG con memory
Gestisce: history della conversazione, costruzione del prompt RAG, streaming.
Usa MAX_TURNS dal config per limitare la history passata al LLM.

Supporta hybrid search (dense + BM25 via RRF) controllato da config.USE_HYBRID.
"""

from app import config
from app.vector_store import cerca_prodotti as cerca_dense
from app.hybrid_search import cerca_prodotti_hybrid
from app.ollama_client import chat


SYSTEM_PROMPT = """Sei ShopBot, l'assistente virtuale di un negozio di articoli sportivi e outdoor.

Regole da seguire SEMPRE:
1. Rispondi SOLO usando i prodotti presenti nel CONTESTO qui sotto.
2. Non inventare prodotti, prezzi o caratteristiche assenti nel contesto.
3. Se la domanda non riguarda prodotti del contesto, dì chiaramente che non hai quel prodotto.
4. Sii conciso, amichevole e utile.
5. Quando citi un prodotto indica sempre il prezzo in euro.
6. Rispondi sempre in italiano.
"""


class ShopBot:
    """
    Chatbot RAG con history della conversazione.

    Flusso per ogni messaggio:
      1. Retrieve  — cerca prodotti rilevanti (hybrid o solo dense)
      2. Augment   — costruisce il prompt con i prodotti come contesto
      3. Generate  — invia a Ollama e streamma la risposta
    """

    def __init__(self):
        self.history: list[dict] = []

    def _build_context(self, prodotti: list[dict]) -> str:
        """Formatta i prodotti trovati come testo leggibile per il LLM."""
        if not prodotti:
            return "Nessun prodotto rilevante trovato nel catalogo per questa domanda."

        lines = ["PRODOTTI DISPONIBILI RILEVANTI:"]
        lines.append("-" * 40)
        for p in prodotti:
            lines.append(f"Nome:        {p['nome']}")
            lines.append(f"Categoria:   {p['categoria']}")
            lines.append(f"Prezzo:      €{p['prezzo']:.2f}")
            lines.append(f"Tag:         {p['tag']}")
            lines.append(f"Descrizione: {p['documento']}")
            lines.append("-" * 40)
        return "\n".join(lines)

    def rispondi(self, domanda: str):
        """
        Elabora la domanda e genera la risposta in streaming.
        Yields stringhe di testo man mano che il modello risponde.
        """
        # 1. RETRIEVE — hybrid (dense+BM25 via RRF) o solo dense, a seconda di config
        if config.USE_HYBRID:
            prodotti = cerca_prodotti_hybrid(domanda)
        else:
            prodotti = cerca_dense(domanda)

        # 2. AUGMENT — il contesto RAG viene inserito nel messaggio utente
        contesto = self._build_context(prodotti)
        user_con_contesto = f"{contesto}\n\nDOMANDA DEL CLIENTE: {domanda}"

        # 3. Costruisci lista messaggi: system + history (limitata) + domanda corrente
        # MAX_TURNS coppie user/assistant = MAX_TURNS * 2 messaggi
        tail = self.history[-(config.MAX_TURNS * 2):]
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            *tail,
            {"role": "user", "content": user_con_contesto},
        ]

        # 4. GENERATE — streaming
        risposta_completa = []
        for chunk in chat(messages, stream=True):
            risposta_completa.append(chunk)
            yield chunk

        # 5. Salva in history la domanda originale (senza contesto) e la risposta
        self.history.append({"role": "user",      "content": domanda})
        self.history.append({"role": "assistant",  "content": "".join(risposta_completa)})

    def reset_history(self):
        """Cancella la history della conversazione."""
        self.history = []
        print("  History conversazione resettata.")
