"""
main.py — CLI ShopBot RAG
Comandi:
  setup  [--reset]  — indicizza prodotti MySQL in ChromaDB
  chat              — chatbot interattivo
  search <query>    — cerca prodotti senza chatbot
  stats             — statistiche
"""

import argparse
import sys
import time

from app import config
from app.db_mysql import get_prodotti_disponibili, get_tutti_i_prodotti
from app.vector_store import reset_collection, indicizza_prodotti, cerca_prodotti, get_stats
from app.chatbot import ShopBot


# ═══════════════════════════════════════════════════════════
# SETUP
# ═══════════════════════════════════════════════════════════

def cmd_setup(reset: bool):
    print("\n╔══════════════════════════════════╗")
    print("║        SHOPBOT — SETUP           ║")
    print("╚══════════════════════════════════╝\n")

    if reset:
        print("▸ Reset collection ChromaDB...")
        reset_collection()

    print("▸ Leggo prodotti disponibili da MySQL...")
    try:
        prodotti = get_prodotti_disponibili()
    except Exception as e:
        print(f"\n❌ Errore connessione MySQL: {e}")
        print("   Assicurati che MySQL sia avviato:")
        print("   docker compose up -d mysql")
        sys.exit(1)

    if not prodotti:
        print("  Nessun prodotto disponibile in MySQL.")
        sys.exit(0)

    print(f"  Trovati {len(prodotti)} prodotti disponibili.\n")
    print("▸ Genero embedding e indicizzо in ChromaDB...")

    try:
        t0 = time.time()
        n  = indicizza_prodotti(prodotti)
        t1 = time.time()
    except Exception as e:
        print(f"\n❌ Errore connessione Ollama: {e}")
        print(f"   Assicurati che Ollama sia avviato su {config.OLLAMA_BASE_URL}")
        print(f"   e che il modello '{config.OLLAMA_EMBED_MODEL}' sia stato scaricato:")
        print(f"   docker compose exec ollama ollama pull {config.OLLAMA_EMBED_MODEL}")
        sys.exit(1)

    print(f"\n✅ Setup completato: {n} prodotti indicizzati in {t1-t0:.1f}s\n")


# ═══════════════════════════════════════════════════════════
# CHAT
# ═══════════════════════════════════════════════════════════

def cmd_chat():
    print("\n╔══════════════════════════════════════════════════╗")
    print("║           SHOPBOT — ASSISTENTE VIRTUALE          ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  Scrivi la tua domanda e premi INVIO.            ║")
    print("║  'esci'  — termina                               ║")
    print("║  'reset' — cancella la history                   ║")
    print("╚══════════════════════════════════════════════════╝\n")

    stats = get_stats()
    if stats["n_prodotti_indicizzati"] == 0:
        print("⚠️  Nessun prodotto indicizzato in ChromaDB.")
        print("   Esegui prima il setup:")
        print("   docker compose run --rm app python -m app.main setup --reset\n")
        sys.exit(1)

    print(f"  {stats['n_prodotti_indicizzati']} prodotti indicizzati — modello: {config.OLLAMA_CHAT_MODEL}\n")

    bot = ShopBot()

    while True:
        try:
            domanda = input("Tu: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  A presto!")
            break

        if not domanda:
            continue

        if domanda.lower() in ("esci", "exit", "quit"):
            print("  A presto!")
            break

        if domanda.lower() == "reset":
            bot.reset_history()
            continue

        print("\nShopBot: ", end="", flush=True)
        try:
            for chunk in bot.rispondi(domanda):
                print(chunk, end="", flush=True)
        except Exception as e:
            print(f"\n❌ Errore Ollama: {e}")
            print(f"   Assicurati che Ollama sia avviato su {config.OLLAMA_BASE_URL}")
        print("\n")


# ═══════════════════════════════════════════════════════════
# SEARCH
# ═══════════════════════════════════════════════════════════

def cmd_search(query: str, top_k: int = 5):
    print(f'\n🔍 Cerco: "{query}"  (top_k={top_k}, max_distance={config.MAX_DISTANCE})\n')

    try:
        risultati = cerca_prodotti(query, top_k=top_k)
    except Exception as e:
        print(f"❌ Errore: {e}")
        sys.exit(1)

    if not risultati:
        print("  Nessun risultato. Hai eseguito il setup?")
        print("  docker compose run --rm app python -m app.main setup --reset")
        return

    print(f"  {len(risultati)} risultati entro distanza {config.MAX_DISTANCE}:\n")
    print(f"  {'#':<3} {'Dist.':<8} {'Nome':<38} {'Cat.':<15} {'€':>7}")
    print("  " + "─" * 74)
    for i, p in enumerate(risultati, 1):
        print(f"  {i:<3} {p['distanza']:<8} {p['nome']:<38} {p['categoria']:<15} {p['prezzo']:>7.2f}")
    print()


# ═══════════════════════════════════════════════════════════
# STATS
# ═══════════════════════════════════════════════════════════

def cmd_stats():
    print("\n📊 STATISTICHE SHOPBOT\n")

    stats = get_stats()
    print(f"  ChromaDB")
    print(f"    Collection  : {stats['collection']}")
    print(f"    Prodotti    : {stats['n_prodotti_indicizzati']}")
    print(f"    Path        : {stats['chroma_path']}")
    print(f"    Max distance: {stats['max_distance']}")

    print(f"\n  MySQL  ({config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DATABASE})")
    try:
        tutti        = get_tutti_i_prodotti()
        disponibili  = [p for p in tutti if p["disponibile"]]
        print(f"    Totale        : {len(tutti)}")
        print(f"    Disponibili   : {len(disponibili)}")
        print(f"    Non dispon.   : {len(tutti) - len(disponibili)}")
    except Exception as e:
        print(f"    ❌ Connessione fallita: {e}")

    print(f"\n  Ollama")
    print(f"    URL       : {config.OLLAMA_BASE_URL}")
    print(f"    Chat      : {config.OLLAMA_CHAT_MODEL}")
    print(f"    Embedding : {config.OLLAMA_EMBED_MODEL}")

    print(f"\n  RAG")
    print(f"    TOP_K        : {config.TOP_K}")
    print(f"    MAX_DISTANCE : {config.MAX_DISTANCE}")
    print(f"    MAX_TURNS    : {config.MAX_TURNS}")
    print()


# ═══════════════════════════════════════════════════════════
# Entry point
# ═══════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        prog="shopbot",
        description="ShopBot RAG — chatbot su catalogo prodotti",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # setup
    p_setup = sub.add_parser("setup", help="Indicizza prodotti MySQL in ChromaDB")
    p_setup.add_argument("--reset", action="store_true",
                         help="Cancella e ricrea la collection prima di indicizzare")

    # chat
    sub.add_parser("chat", help="Avvia il chatbot interattivo")

    # search
    p_search = sub.add_parser("search", help="Cerca prodotti senza il chatbot")
    p_search.add_argument("query", help='Testo da cercare, es. "scarpe impermeabili"')
    p_search.add_argument("--top-k", type=int, default=5, dest="top_k",
                          help="Numero max di risultati (default: 5)")

    # stats
    sub.add_parser("stats", help="Mostra statistiche")

    args = parser.parse_args()

    if args.command == "setup":
        cmd_setup(reset=args.reset)
    elif args.command == "chat":
        cmd_chat()
    elif args.command == "search":
        cmd_search(args.query, top_k=args.top_k)
    elif args.command == "stats":
        cmd_stats()


if __name__ == "__main__":
    main()
