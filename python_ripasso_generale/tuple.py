# Esercizio 1 — Creazione e accesso (Facile)
# Crea una tupla chiamata mesi contenente i nomi dei 12 mesi dell'anno. Poi: (a) stampa il terzo mese; (b) stampa l'ultimo mese usando 
# l'indicizzazione negativa; (c) stampa quanti elementi contiene la tupla con len(); (d) verifica con type() che sia effettivamente una tupla.

# mesi = "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
# print(mesi[2])
# print(mesi[-1])
# print(len(mesi))
# print(type(mesi))

# Esercizio 2 — Immutabilità (Facile)
# Crea una tupla colori = ("rosso", "verde", "blu"). Prova a: (a) modificare il secondo elemento e osserva l'errore; (b) convertirla in lista con 
# list(), aggiungi "giallo", poi riconvertila in tupla con tuple(). Stampa il risultato finale.
# colori = ("rosso", "verde", "blu")
# colori_lista=list(colori)
# colori_lista.append("giallo")
# colori= tuple(colori_lista)
# print(colori)
# print(colori_lista)

# Esercizio 3 — Tuple unpacking (Medio)
# Data la tupla persona = ("Mario", "Rossi", 30, "Milano"), spacchettala in quattro variabili: nome, cognome, eta, citta. Poi stampa una frase 
# del tipo: "Mario Rossi ha 30 anni e abita a Milano" usando le variabili.

# persona = ("Mario", "Rossi", 30, "Milano")
# n,c,eta,cit=persona
# print(n)
# print(c)
# print(eta)
# print(cit)
# print(f"{n} {c} ha {eta} anni e abita a {cit}")

# Esercizio 4 — Funzione con tupla (Medio)
# Scrivi una funzione statistiche(numeri) che accetta una lista di numeri e restituisce una tupla con tre valori: il minimo, il massimo e la 
# media. Testa la funzione con la lista [4, 7, 2, 9, 1, 5, 8, 3, 6] e spacchetta il risultato in tre variabili separate
# numeri = [4, 7, 2, 9, 1, 5, 8, 3, 6]

# def statistiche(numeri):
#     if not numeri:
#         raise ValueError("La lista non può essere vuota")
#     media = sum(numeri) / len(numeri)
#     return min(numeri), max(numeri), media

# minimo, massimo, media_numeri = statistiche(numeri)
# print(minimo, massimo, media_numeri)

# esercizio 5 — Swap e zip (Medio-Avanzato)
# Hai due liste: nomi = ["Alice", "Bob", "Carlo"] e voti = [8, 6, 9]. (a) Usa lo swap con tuple per invertire il primo e l'ultimo elemento di voti. (b) 
# Usa zip() per creare una lista di tuple (nome, voto). (c) Ordina questa lista per voto decrescente usando sorted() con key=lambda x: x[1], 
# reverse=True.

nomi = ["Alice", "Bob", "Carlo"]
voti = [8, 6, 9]

voti[0],voti[2]=voti[2],voti[0]
print(voti)
lista = list(zip(nomi, voti))



#lambda parametro: risultatoprint(lista)
lista2=sorted(lista, key=lambda x: x[1], reverse=True)
print(lista2)