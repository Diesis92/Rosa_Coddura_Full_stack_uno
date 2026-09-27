# dati_utente={
#     "nome":"Mario",
#     "cognome": "Rossi" ,
#     "eta": 40,
#     "citta":"Milano",
#     "professione":"artigiano",
#     "figli":["tizio","caio","sempronio"] 
# }

# for k in dati_utente:
#     print("chiave:", k," Valore:", dati_utente[k])
  
# dati_utente["Genere"] = "M"
# print(dati_utente)

# print(dati_utente.keys())
# print(dati_utente.values())
# print(list(dati_utente.values()))

# team={
#     "titolare":{"nome": "Teo", "cognome": "Bianchi", "ruolo": "CEO"},
#     "impiegato":{"nome": "Valerio", "cognome": "Celesti", "ruolo": "Social Media Manager"} 
# }

# # valore_rimosso= team.pop("impiegato")
# # print(valore_rimosso)
# print(team["impiegato"]["cognome"])

# Rubrica telefonica
# Crea un dizionario chiamato rubrica con almeno 4 contatti (nome 
# →
#  numero di telefono come stringa). Stampa il numero di un contatto 
# specifico. Poi aggiungi un nuovo contatto e stampa tutta la rubrica.

# rubrica={"Mario": "091252135",
#          "Marisa": "339406704",
#          "Giulio": "091242136",
#          "Rosa": "3505009993",
#         }

# print(rubrica["Rosa"])
# rubrica["Tiziana"]="3394079204"
# print(rubrica)


# Conteggio parole
# Data la frase "il gatto mangia il topo e il cane guarda", crea un dizionario che conti quante volte appare ogni parola. Stampa il risultato. 
# Suggerimento: scorri le parole con un ciclo for e usa in per controllare se la chiave esiste già.
# frase= "il gatto mangia il topo e il cane guarda"
# parole=frase.split()
# conteggio={}

# for parola in parole:
#     if parola in conteggio:
#         conteggio[parola]+=1
#     else:
#         conteggio[parola]=1
# print(conteggio)


# Scheda studente
# Crea un dizionario studente con le chiavi: nome, cognome, voti (lista di interi), promosso (booleano). Calcola la media dei voti e aggiungila 
# al dizionario come chiave media. Stampa il dizionario completo.

# studente = {
#     "nome": "Mario",
#     "cognome": "Rossi",
#     "voti": [7, 8, 6, 9]
# }
# # 12345 somma elementi
# # 15/5=3
# media = sum(studente["voti"]) / len(studente["voti"])

# calcolo per ottnere la media senza sum()
# somma = 0

# for voto in studente["voti"]:
#     somma += voto

# media = somma / len(studente["voti"])

# print(media)
# print(media)
# studente["media"]=7.5
# print(studente)

# Dizionario annidato
# Crea un dizionario biblioteca dove ogni chiave è il titolo di un libro e il valore è un dizionario con autore, anno e pagine. Inserisci almeno 3 
# libri. Stampa autore e anno per ogni libro usando un ciclo for.

# biblioteca = {
#     "Il nome della Rosa": {
#         "autore": "Umberto Eco",
#         "anno": 1980,
#         "pagine": 503
#     },

#     "1984": {
#         "autore": "George Orwell",
#         "anno": 1949,
#         "pagine": 328
#     },

#     "Il Signore degli Anelli": {
#         "autore": "J.R.R. Tolkien",
#         "anno": 1954,
#         "pagine": 1216
#     }
# }
# for libro in biblioteca:
#     print("Libro", libro),
#     print("autore", biblioteca[libro]["autore"]),
#     print("anno", biblioteca[libro]["anno"]),

# 5
# Gestione inventario
# Crea un dizionario magazzino con prodotti e quantità. Scrivi un programma che: (1) stampa tutti i prodotti con quantità zero, (2) rimuove 
# con .pop() un prodotto esaurito, (3) aggiunge un nuovo prodotto, (4) stampa la lista ordinata delle chiavi.

magazzino = {
    "mele": 20,
    "pane": 15,
    "latte": 10,
    "pasta": 25,
    "patate":0
}

for prodotto in magazzino:
    if magazzino[prodotto]== 0:
        print(prodotto)

prodotto_rimosso= magazzino.pop("patate")
print(prodotto_rimosso)

magazzino["farina"]=10


print(sorted(magazzino))
