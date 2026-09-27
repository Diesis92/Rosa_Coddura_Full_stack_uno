# # def fattoriale(n):
   
# #     if n == 0: case base 1
# #         return 1   # 0! = 1 per definizione
# #     i = 1
# #     fatt = 1  # elemento neutro per la moltiplicazione visto che il fattoriale si calcola un passo alla volta
# #     while i <= n:
# #         fatt *= i
# #         i += 1
# #     return fatt
# # print(fattoriale(4))   # 
# # →
# #  24
 
# #  4 è uguale a 0 non
# #  entra nel ciclo
# #  1 è minore di 4= sì
# #  1*1=1
# #  i=2 
# # print(fattoriale(0))   # 
# # →
# #  1
# #  ah ho capito fa tutto il giro fino ad arrivare a 4
# #  1*2*3*4
# #  1*2=2
# #  2*=3=6
# #  6*4=24
 
# #  se volessi il simbolo della moltip0licazione
# #  i = 1

# # i = 1

# # while i <= 1:
# #     j = 1
# #     while j <=10:
# #         print(i, "x", j )
# #         j+=1
# #     i+=1
    
    
    
# # Conto alla Rovescia
# # Scrivi una funzione conto_alla_rovescia(n) 
# # che stampa i numeri da n fino a 1, poi 
# # stampa "Boom!


# def conto_alla_rovescia(n):
#     i = n
#     while i >= 1:
#         print(i)
#         i -= 1
#     print("Boom!")
    
# print(conto_alla_rovescia(10))


# # Potenze di 2
# # Scrivi un ciclo che stampa tutte le potenze di 
# # 2 minori di 1000: 1, 2, 4, 8, 16... Hint: 
# # moltiplica per 2 ad ogni giro!

# i=1
# while i <1000:
#     print(i)
#     i*=2
    
# # Somma dei Pari
# # Scrivi una funzione somma_pari(n) che 
# # calcola la somma di tutti i numeri pari da 0 a 
# # n compreso. Usa l'operatore modulo % per 
# # capire se un numero è pari.

# # def somma_pari(n):
# #     i=0
# #     while i>=0:
# #         if i % 2 ==0:
# #             print(i)
# #         i+=i
# # print(somma_pari(10))



# def somma_pari(n):

#     i = 0
#     somma = 0

#     while i <= n:

#         if i % 2 == 0:
#             print(i)
#             somma += i

#         i += 1

#     return somma

# print(somma_pari(10))


# indovina il Numero
# Simula un gioco: hai un numero segreto (es. 7). Il "giocatore" parte da 
# 1 e incrementa di 1. Usa il break per fermarti quando raggiungi il 
# numero segreto e stampa quanti tentativi ci sono voluti.

# segreto=7
# contatore=0
# while True:
#     tentativi = int(input("Indovina il numero!\n Scrivi un numero: "))
#     contatore+=1
#     if tentativi !=segreto:
#         print("Ritenta, hai sbagliato!")
#     if tentativi == segreto:
#         print("Hai indovinato")
#         print("Trovato in", contatore, "tentativi")
#         break
    
# Triangolo Invertito 
# ★
# Scrivi una funzione stelle_inverse(n) che per n=5 stampa: *****, ****, 
# ***, **, *. (Parte da n stelle e scende a 1.)

# def conta(n):
#     i=n #parto dal numero che passo come argomento
#     while i>=0: #valuto se è maggiore uguale di zero
#         print(i)
#         i-=1#decremento
# print(conta(5))

# def stelle_inverse(n):
#     i=n
#     while i>=1: #5 è maggiore o uguale a 1? True
#         print("*"*i)
#         i-=1
# print(stelle_inverse(5))

# # In avanti: parto dal basso (0) e aumento i.

# # All'indietro: parto dall'alto (n) e diminuisco i.
# def candele(n):
#     i=1
#     while i<=n: #1 è minore o uguale a 6? True
#         print("i" * i)
#         i+=1
# print(candele(6))

def stampa_lista(L):
    i=0
    risultato = ""
    while i <len (L):
        risultato += str(L[i])
        i+=1
    return risultato
    
print(stampa_lista([1,3,4,5,6,7]))




