#[operazione, for, variabile temporanea, in, interable]
#[num **2 for num in lista]
# lista=[10,100,1000]
# L=[num/10 for num in lista]
# print(L)
# L=[num/10 for num in range(10,21)]
# print(L)
# nomi=["Andrea","Marco","Luigi"]
# #nome variabile appoggio=[nomi.metodo for variabile temp in variabile lista]
# N=[nome.upper() for nome in nomi]
# print(N)
# inizialeG=[nome for nome in nomi if nome.startswith("L")]
# print(inizialeG)
# condizioni_multiple=[nome for nome in nomi if nome.startswith("L")and len(nome)>4]
# print(condizioni_multiple)


# parola= "Python"
# Le=[lettera.upper() for lettera in parola]
#logica if
#[espressione for elemento in iterabile if condizione]
# numeri=[5,10,2,20,14,3]
# maggior_10=[num for num in numeri if num > 10]
# print(maggior_10)

# ⭐
#  Livello 1 — Quadrati Perfetti
# Crea una List Comprehension che generi i quadrati dei numeri da 1 a 10.
# # Risultato atteso: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# quadrati=[numero ** 2 for numero in range(1,11) ]
# print(quadrati)

#  ⭐⭐
#  Livello 2 — Filtro Pari
# Data la lista [3, 7, 2, 8, 5, 14, 11, 6], estrai solo i numeri pari usando una List Comprehension con condizione if.
# # Risultato atteso: [2, 8, 14, 6]
# listaN=[3, 7, 2, 8, 5, 14, 11, 6]
# nuovaL=[num for num in listaN if num % 2 == 0]
# print(nuovaL)

# ⭐⭐⭐
#  Livello 3 — Normalizzazione
# Data la lista [10, 20, 30, 40, 50], crea una nuova lista dove ogni elemento è diviso per il massimo della lista (max(lista)), ottenendo valori tra 
# 0 e 1.
# # Risultato atteso: [0.2, 0.4, 0.6, 0.8, 1.0]
n=[10, 20, 30, 40, 50]
num=[numero / max(n) for numero in n]
print(num)