#scrivi def
#ciclo for range più metodo len per parametro
#printa il risultato

# def stampa_lista(L):
  
#     for i in range(len(L)):
#        print(i, L[i])
    
# (stampa_lista([1,2,3,4,]))

# def lista(l):
#     for i, x in enumerate(l):
#         print(i,x)
        
# lista(["uno", "due", "tre"])
    
    


# controllo per vedere se la lista è vuota. se è vuota ritorna 0
# se ci sono elementi, crea una variabile somma e inizializzala a 0
#Iteriamo sulla lista e prendiamo ogni elemento, mettendolo nella variabile x, per poi aggiungerlo alla variabile somma
#dopo eseguiamo la media catturandola in una variabile media il cui calcolo sarà somma diviso la lunghezza della lista e ritorniamo la media


# def trova_media(m):
#     if len(m) == 0:
#         return 0
#     somma = 0
#     for i in m:
#         somma +=i
#     media = somma / len(m)
#     return media 
# print(trova_media([1,4,6,8,9]))

#Funzione: conta stringhe per lettera iniziale
#funzione con due parametri
#contatore
#for
# variabile iniziale la conforntiamo con l'elemtno che scorre il for e mettimao il meto lower

# incremento
# return
# lista
# print

# def conta_stringhe(l,c):
#     contatore=0
#     for i in l:
#         iniziale = i[0].lower()
#         if iniziale == c.lower():
#              contatore += 1
#     return contatore
    
# lista = ["Albero", "Uva", "Acero", "Banana", "Amarena"]
# print(conta_stringhe(lista, "a"))

#flag

# definisci def
#flag
#ciclo for 
#
#inverti boolean flag
#fuori if, return variabile flag
    
# def dubbio(d):
#     is_negative= False
#     for x in d:
#         if x < 0:
#             is_negative = True
#     return is_negative
# l=[4,8,9,-5]
# print(dubbio(l))

# def dubbio(d):
#     is_negative= False
#     somma = 0
#     for x in d:
#         somma+=x
#         if not is_negative and x < 0:
#             is_negative = True
    
#     return somma, is_negative
# l=[4,8,9,-5]
# print(dubbio(l))

#Esercizio: Unione di due liste senza duplicati
#def
#copia L1
#for per L2
#se x non è in risultato
#appendo al risltato
#ordino
#ritorno il risultato

# def unione(L1,L2):
#     risultato = list(L1)
#     for x in L2:
#         if x not in risultato:
#             risultato.append(x)
#         risultato.sort()
#     return risultato

# def unione(L1,L2):
#     risultato = list(L1)
#     for x in L1 + L2:
#         if x not in risultato:
#             risultato.append(x)
#         risultato.sort()
#     return risultato
# print(unione([1,2,3,4], [1,2,7,9]))

# # Esercizio 1 — Trova il massimo
# # Scrivi una funzione trova_massimo(L) che, senza usare la funzione built-in max(), scorra la lista e restituisca l'elemento più grande. Gestisci 
# # il caso di lista vuota.

# def trova_massimo(L):
#     if len(L) == 0:
#         return 0
#     massimo = L[0]
#     for x in L:
#         if x>massimo:
#             massimo = x
#     return massimo
# print(trova_massimo([2,4,6,8,10]))
        
# Esercizio 2 — Conta pari e dispari
# Scrivi una funzione conta_pari_dispari(L) che accetti una lista di interi e restituisca due valori: il numero di elementi pari e il numero di 
# elementi dispari

# def conta_pari_dispari(L):
#     if len(L) == 0:
#             return 0
#     pari = 0
#     dispari = 0
#     for x in L:
#         if  x % 2 == 0:
#             pari +=1
#         else:
#             x % 2 != 0
#             dispari +=1
#     return pari, dispari
# print(conta_pari_dispari([1,4,5,8,7,10]))
         
    


# Esercizio 3 — Inverti una lista
# Scrivi una funzione inverti(L)f che, senza usare reversed() né il metodo .reverse(), restituisca una nuova lista con gli elementi in ordine 
# inverso.

# def inverti(L):
#     reverse = L[::-1]
#     return reverse
# print(inverti([1,2,3,4,5]))

# def inverti(L):
#     risultato = []
#     for x in range(len(L)-1,-1,-1):
#         risultato.append(L[x])
#     return risultato
# print(inverti([1,2,3,4,5]))
    

# Esercizio 4 — Lista senza duplicati
# Scrivi una funzione rimuovi_duplicati(L) che accetti una lista e restituisca una nuova lista con gli stessi elementi ma senza ripetizioni, 
# mantenendo l'ordine di prima apparizione.

# def rimuovi_duplicati(L):
#     if len(L)==0:
#         return 0
#     risultato = []
#     for x in L:
#         if x not in risultato:
#             risultato.append(x)
#     return risultato
# print(rimuovi_duplicati([1,2,3,2,1,6,7,9,10]))


# Esercizio 5 — Bandiera: lista palindroma
# Scrivi una funzione è_palindroma(L) che usi una bandiera per controllare se una lista è palindroma (si legge uguale da sinistra a destra e da 
# destra a sinistra). Usa enumerate per confrontare elementi simmetrici.

# def è_palindroma(L):
#     if len(L)==0:
#         return 0
#     palindroma = True
#     for i, x in enumerate(L):
#         #“se x è diverso dall'elemento di L all'indice -i-1”
#         if x != L[-i-1]:
#             palindroma = False
#     return palindroma
# frase ="i topi non avevano nipoti".replace(" ","")
# print(è_palindroma(frase))
    
i = 0

while i < 5:
    i += 1

print(i)
    