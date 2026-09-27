# Creazione e Indicizzazione
# Crea una lista chiamata numeri contenente: 10, 25, 3, 87, 42, 16.
# Stampa il primo elemento, l'ultimo elemento (con indice negativo), e la 
# sotto-lista dal secondo al quarto elemento.
# numeri = [10, 25, 3, 87, 42, 16]
# print(numeri[0])
# print(numeri[-1])
# print(numeri[1:4])

# Sort e Ricerca
# Crea la lista voti = [28, 18, 30, 22, 25, 19, 27].
# Ordinala in modo crescente, poi decrescente. Usa l'operatore in per 
# verificare se il voto 30 è presente, poi usa index() per trovarne la 
# posizione.

# voti = [28, 18, 30, 22, 25, 19, 27]
# voti.sort()
# print(voti)
# voti.sort(reverse=True)
# print(voti)
# if 30 in voti:
#     print("esiste")
# print(voti.index(30))

# Liste Miste e Annidate
# Crea una lista mista che contenga: un intero, una stringa, una lista di 
# tre numeri, e un float.
# Stampa la lunghezza di mista, poi accedi al secondo elemento della 
# lista interna.

# mista = [1, "due", [3,4,5], 6.2]
# print(len(mista))
# print(mista[2][1])

# Raddoppia con il While
# Crea la lista valori = [3, 7, 11, 15, 19].
# Usando un ciclo while, raddoppia ogni elemento della lista. Stampa la 
# lista prima e dopo l'operazione.

# valori = [3, 7, 11, 15, 19]
# print(valori)

# i = 0
# while(i<len(valori)):
#     valori[i]=valori[i]*2
#     i = i+1
# print(valori)


# Append vs Extend
# Parti da a = [1, 2, 3] e b = [4, 5, 6].
# Crea una copia c = [1, 2, 3].
# Usa append su a con b e extend su c con b. Stampa entrambe e 
# spiega la differenza.

# a = [1, 2, 3]
# b = [4, 5, 6]
# c=a.copy()
# print(c)
# a.append(b)
# c.extend(b)
# print(a)
# print(c)

# Pop e Gestione Elementi
# Crea la lista frutta = ["mela","banana","pera","kiwi","uva"].
# Rimuovi l'ultimo elemento salvandolo in una variabile e stampalo. Poi 
# rimuovi il secondo elemento (indice 1). Stampa la lista finale.

# frutta = ["mela","banana","pera","kiwi","uva"]
# ultimo = frutta.pop()
# print(ultimo)
# secondo = frutta.pop(1)
# print(secondo)

# print(frutta)

# Range e Somma
# Usa range() per creare la lista dei multipli di 5 da 5 a 100 incluso.
# Scorri la lista con un while e calcola la somma di tutti gli elementi. 
# Stampa il risultato.

# multipli=list(range(5,101,5))
# print(multipli)

# risultato = 0  # accumula la somma
# i = 0          # tiene traccia dell'indice\
# while(i<len(multipli)):
#     risultato=risultato + multipli[i]
#     i+=1
# print(risultato)


# Split e Manipolazione
# Hai la stringa s = "Python:Java:C++:JavaScript:Rust".
# Usa split() per ricavare una lista di linguaggi. Stampa il numero di 
# linguaggi, ordinali alfabeticamente e stampa il primo e l'ultimo.

# s = "Python:Java:C++:JavaScript:Rust"
# lista= s.split(":")
# print(lista)
# lista.sort()
# print(lista)
# print(lista[0])
# print(lista[-1])


# Esercizio 1 — Crea e Indicizza
# Crea una lista numeri contenente i seguenti valori: 5, 12, "Python", 3.14, True, [1, 2].
# Stampa: il primo elemento, l'ultimo elemento (usando indice negativo), il terzo elemento, e i primi tre elementi usando lo slicing.
numeri=[5, 12, "Python", 3.14, True, [1, 2]]
print(numeri[0])
print(numeri[-1])
print(numeri[2])
print(numeri[0:3])
