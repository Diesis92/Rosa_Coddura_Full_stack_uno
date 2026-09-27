


# frutta=set(["mela", "banana", "kiwi", "mela","banana"])
# print(frutta)

# lettere=set("televisione")
# print(lettere)
#metodi set:
#add
#remove
#discard
# in operator
# mio_set={1,2,3,2,1}
# print(mio_set)
# mio_set.add(4)
# print(mio_set)

# mio_set.remove(5)
# print(mio_set)


# mio_set.discard(5)
# print(mio_set)

# mio_set.remove(1)
# print(mio_set)

# print(1 in mio_set)

# lista città
# ocnversione lista in set

# stampa con f string la lunghezza di  città

# citta = [
#     "Palermo",
#     "Roma",
#     "Milano",
#     "Napoli",
#     "Torino",
#     "Palermo",
#     "Roma",
#     "Milano",
#     "Napoli",
#     "Torino"
# ]

# citta_uniche=set(citta)
# print(citta_uniche)
# print(f"Attualmente i nostri ordini arrivano da {len(citta_uniche)} citta"  )


#lista log eventi ripetuti
# conversione
# stamp len
# ciclo for 

log_eventi = [
    "LOGIN",
    "LOGOUT",
    "LOGIN",
    "ERRORE",
    "DOWNLOAD",
    "LOGIN",
    "ERRORE",
    "UPLOAD",
    "LOGOUT",
    "LOGIN"
]

log_unici=set(log_eventi)
print(f"abbiamo avuto numero {len(log_unici)} eventi")

for evento in log_unici:
    print(f"---> {evento}")
    
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # {1, 2, 3, 4, 5, 6}
print(A & B)  # {3, 4}
print(A - B)  # {1, 2}
print(A ^ B)  # {1, 2, 5, 6