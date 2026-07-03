"""
chatbot.py — Chatbot RAG con memory

Gestisce:
- history della conversazione
- retrieval (Hybrid Search oppure Dense Search)
- costruzione del prompt RAG
- streaming della risposta

IMPORTANTE:
Se il retrieval non restituisce prodotti, il modello NON viene chiamato,
così non può inventare prodotti inesistenti.
"""

from app import config
from app.vector_store import cerca_prodotti as cerca_dense
from app.hybrid_search import cerca_prodotti_hybrid
from app.ollama_client import chat


SYSTEM_PROMPT = """Sei ShopBot, l'assistente virtuale di un negozio di articoli sportivi e outdoor.

Regole IMPORTANTI:
- Rispondi ESCLUSIVAMENTE usando i prodotti presenti nel contesto.
- Non inventare mai prodotti, prezzi o caratteristiche.
- Se il contesto è vuoto, significa che il catalogo NON contiene prodotti adatti.
- Non proporre alternative non presenti nel contesto.
- Quando citi un prodotto indica sempre il prezzo.
- Rispondi sempre in italiano.
"""


class ShopBot:

    def __init__(self):
        self.history = []

    def _build_context(self, prodotti):

        lines = ["PRODOTTI DISPONIBILI:"]
        lines.append("-" * 40)

        for p in prodotti:
            lines.append(f"Nome: {p['nome']}")
            lines.append(f"Categoria: {p['categoria']}")
            lines.append(f"Prezzo: €{p['prezzo']:.2f}")
            lines.append(f"Tag: {p['tag']}")
            lines.append(f"Descrizione: {p['documento']}")
            lines.append("-" * 40)

        return "\n".join(lines)

    def rispondi(self, domanda):

        # -------------------------
        # RETRIEVAL
        # -------------------------

        if config.USE_HYBRID:
            prodotti = cerca_prodotti_hybrid(domanda)
        else:
            prodotti = cerca_dense(domanda)

        # --------------------------------------------------
        # FIX PRINCIPALE:
        # Se non ci sono prodotti NON chiamare il modello.
        # --------------------------------------------------

        if not prodotti:

            risposta = (
                "Mi dispiace, non ho trovato prodotti nel catalogo "
                "che soddisfano la tua richiesta."
            )

            self.history.append(
                {
                    "role": "user",
                    "content": domanda,
                }
            )

            self.history.append(
                {
                    "role": "assistant",
                    "content": risposta,
                }
            )

            yield risposta
            return

        # -------------------------
        # COSTRUZIONE CONTESTO
        # -------------------------

        contesto = self._build_context(prodotti)

        user_message = (
            f"{contesto}\n\n"
            f"DOMANDA DEL CLIENTE:\n{domanda}"
        )

        history = self.history[-config.MAX_TURNS * 2 :]

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            *history,
            {
                "role": "user",
                "content": user_message,
            },
        ]

        # -------------------------
        # GENERAZIONE
        # -------------------------

        risposta = ""

        for chunk in chat(messages, stream=True):
            risposta += chunk
            yield chunk

        # -------------------------
        # HISTORY
        # -------------------------

        self.history.append(
            {
                "role": "user",
                "content": domanda,
            }
        )

        self.history.append(
            {
                "role": "assistant",
                "content": risposta,
            }
        )

    def reset_history(self):
        self.history = []
        print("History conversazione resettata.")