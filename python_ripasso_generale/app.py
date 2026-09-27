# # a = 99
# # b=6

# # if(a>b+30): #b+30=36. 99>36?true
# #     print("La condizione è vera")
# #     a = a *2 
# #     print("il valore di a è",a)#198
# # print("il  porgramma è finito")
# # #python app.py

# # def num_alto(a,b):
# #     if(a>b):
# #         return a
# #     return b
# # print(num_alto(10,5))

# # def nome(nome):
# #     prima_lettera=nome[0]
# #     if prima_lettera == "R":
# #         return True
# #     return False

# # def nome_d(nomed):
# #     return nome[0]=="R"

# # def nome_t(nomet):
# #     prima_lettera=nome[0]
# #     if prima_lettera == "A":
# #         return True
# #     else:
# #         if prima_lettera=="N":
# #             return True
# #         return False

# # def nome_q(nomeq):
# #     prima_lettera=nome[0]
# #     if prima_lettera == "A":
# #         return True
# #     elif prima_lettera == "B":
# #         return True
# #     return False

# #quanti giorni ha un mese

# def bisestile(anno):
#     if(anno % 4 == 0 and anno % 100 != 0) or anno % 400 ==0:
#         return True
#     return False
# def giorni(mese, anno=1):
#     if type(mese)!= int:
#         print("Mese non valido")
#         return
#     if not(1<=mese<=12):
#         print("ma dai, non sia i mesi?!?")
#         return

#     if(mese == 2):
#         if(bisestile(anno)):
#             return 29
#         return 28
#     elif mese in[4,6,9,11]:
#         return 30
#     return 31
# print(bisestile(2025))
# print(giorni(5,2025))

    
# def voto_lettera(voto):
#     if voto < 6:
#         print("insufficiente")
#     elif voto  == 6:
#         print("sufficiente")
#     elif voto ==7:
#         print("buono")
#     elif voto == 8 or voto == 9:
#         print("distinto")
#     elif voto == 10:
#         print("ottimo")
#     else:
#         print("Non valido")

 
# # Calcolatrice semplice
# # Scrivi una funzione calcola(a, op, b) che riceve due numeri e un operatore (stringa: "+", "-", "*", "/") e restituisce il risultato. Gestisci la 
# # divisione per zero restituendo None.
# #controllo di a e b in int e float
# def calcola(a,op,b):
#     if  type(a) not in [int, float]:
#         print("deve essere un numero!")
#         return
#     if  type(b) not in [int, float]:
#         print("deve essere un numero!")
#         return
#     if op == "/" and b == 0:
#         print("non puoi dividere un numero per zero")
#         return
#     if op == "+":
#         return a + b
#     elif op == "-":
#         return a - b
#     elif op == "*":
#             return a - b
#     elif op == "/":
#             return a - b
#     else:
#         print("valore non valido!")

# # Triangolo valido
# # Scrivi una funzione triangolo_valido(a, b, c) che restituisce True se i tre lati formano un triangolo valido (ogni lato deve essere minore della 
# # somma degli altri due) e False altrimenti
# def triangolo_valido(a,b,c):
#     if a <= 0 or b <= 0 or c <=0:
#         return False
#     if  a<b+c and  b<a+c and c<a+b:
#         return True
#     return False
        
    
    
# # FizzBuzz
# # Scrivi una funzione fizzbuzz(n) che restituisce:
# # "FizzBuzz" se n è divisibile per 3 e per 5
# # "Fizz" se divisibile solo per 3
# # "Buzz" se divisibile solo per 5
# # il numero stesso (come stringa) altrimenti

# def FizzBuzz(n):
#     if not type(n) == int:
#         print("deve essere numero intero")
#         return
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#         return
#     elif n % 3 == 0:
#         print("Fizz")
#         return
#     elif n % 5 == 0:
#         print("Buzz")
#         return
#     return str(n)

# Massimo tra tre (senza usare max())
# Scrivi una funzione massimo_tre(a, b, c) che restituisce il valore più grande tra tre numeri usando solo if/elif/else, senza usare la funzione 
# built-in max().

# def massimo_tre(a,b,c):
#     if  a > b and a > c:
#         return a
#     elif  b > a and b > c:
#         return b
#     else:
#         return c
    
# print(massimo_tre(5,2,3))
    

# FUNZIONE estrai_testo(testo, marcatore)

#     pos1 ← posizione del primo "marcatore" all'interno di "testo"

#     pos2 ← posizione del secondo "marcatore" all'interno di "testo"
#            cercandolo a partire dalla posizione:
#            pos1 + lunghezza di "marcatore"

#     inizio ← pos1 + lunghezza di "marcatore"

#     stringa ← parte di "testo" compresa tra "inizio" e "pos2"
#                escluso il carattere/il testo presente in "pos2"

#     RESTITUISCI stringa

# FINE FUNZIONE

        

# def estrai_testo(testo, marcatore):
#     pos1 = testo.find(marcatore)
#     pos2= testo.find(marcatore, pos1+len(marcatore))  
#     stringa = testo[pos1+len(marcatore):pos2]
#     return stringa

# print(estrai_testo("Era una notte *buia* e tempestosa","*"))

# "E r a _ u n a _ n o t t e _ * b u i a * _ e..."
#  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
 
#  14 marcatore
#  pos1=14
#  pos1=14+1=15
#  15
#  pos2=19
#  15:19
 


# def estrai_testo(testo, marcatore):
#     p1=testo.find(marcatore)
#     p2=testo.find(marcatore, p1+len(marcatore))
#     stringa=testo[ p1+len(marcatore):p2]
#     return stringa
# print(estrai_testo("si sta come *d'autunno* sugli alberi le foglie", "*"))





def estrai_testo(testo, marcatore):
    p1=testo.find(marcatore)
    p2=testo.find(marcatore,p1+len(marcatore))
    stringa=testo[p1+len(marcatore):p2]
    return stringa

print(estrai_testo("La donzelletta *vien* dalla campagna", "*"))

# Exercise 1 — Saluto Personalizzato (
# ⭐
#  Facile)
# Scrivi una funzione chiamata saluta che accetta un parametro nome e restituisce la stringa "Ciao, [nome]!". Chiamala con il tuo nome e stampa il 
# risultato.

def saluta(nome):
   return f"Ciao {nome}"
print(saluta("Rosa"))

# Exercise 2 — Area del Rettangolo (
# ⭐
#  Facile)
# Scrivi una funzione area_rettangolo(base, altezza) che restituisce l'area di un rettangolo. Testa la funzione con base=5 e altezza=3.

def area_rettangolo(base, altezza):
    return base * altezza
print(area_rettangolo(5,3))

# Exercise 3 — Valore Assoluto (
# ⭐⭐
#  Medio)
# Scrivi una funzione valore_assoluto(n) che restituisce il valore assoluto di un numero senza usare la funzione built-in abs(). Usa solo un 
# confronto con zero.

def valore_assoluto(n):
    if n < 0:
        return -n
    return n
print(valore_assoluto(-5))
   
    
# Exercise 4 — Conta Vocali (
# ⭐⭐
#  Medio)
# Scrivi una funzione conta_vocali(testo) che riceve una stringa e restituisce il numero di vocali (a, e, i, o, u) presenti, ignorando 
# maiuscole/minuscole.

def conta_vocali(testo):
   vocali = "aeiou"
   contatore = 0
   for lettera in testo.lower():
       if lettera in vocali:
           contatore +=1
   return contatore
print(conta_vocali("il cielo in una stanza")) #8
    
        
# Exercise 5 — Saluto con Default (
# ⭐⭐
#  Medio)
# Scrivi una funzione saluta_formale(nome, titolo="Sig.") che restituisce "Buongiorno, Sig. Rossi" (o il titolo passato). Il parametro titolo deve 
# avere un valore di default.



def saluta_formale(nome,titolo="Sig."):
    return f"Buongiorno, {titolo} {nome}"
print(saluta_formale("Rossi"))
print(saluta_formale("Bianchi", "Dr."))

# Exercise 6 — Fattoriale Ricorsivo (
# ⭐⭐⭐
#  Difficile)
# Scrivi una funzione fattoriale(n) che calcola il fattoriale di un numero intero positivo. Usa un ciclo for (non la ricorsione). Verifica che fattoriale(5) 
# restituisca 120.
# Exercise 7 — Estrai Dominio Email (
# ⭐⭐⭐
#  Difficile)
# Scrivi una funzione estrai_dominio(email) che riceve una stringa email (es. "mario@example.com") e restituisce solo il dominio (es. 
# "example.com"). Usa il metodo .split().
# 💡
#  Consiglio: scrivi prima la firma della funzione (def ...), poi il corpo, e infine testa con almeno due casi diversi
    
   #la funzione ricorsiva chiama se stessa all'interno dello scope della funzione stessa
   #si ocnfront il numero con 0
   
# Esercizio 1 — Riscaldamento (stesso schema del fattoriale)
# Scrivi una funzione somma_da_1_a_n(n) che calcola la somma di tutti i numeri interi da 1 a n (es. somma_da_1_a_n(5) deve dare 15, cioè 1+2+3+4+5). 
# Prova prima con il ciclo for, poi — se ti va — anche con la ricorsione. È identico allo schema del fattoriale, ma con + al posto di *.

# def fatto(n):
#     acc = 0
#     for numeri in range (1, n+1):
#         acc = acc + numeri
#     return acc
# print(fatto(5))

# def fattr(n):
#     if n == 0:
#         return 0
#     return n+fattr(n-1)
# print(fattr(5))

# Esercizio 2 — Torniamo a Fibonacci (Passaggio 2)
# Scrivi fibonacci(n) che calcola l'n-esimo numero della successione di Fibonacci (0, 1, 1, 2, 3, 5, 8, ...), usando la ricorsione. 
# Qui dovrai ricordarti una cosa importante che abbiamo visto: quanti casi base servono, e perché (non uno solo come nel fattoriale).

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo (fibo-1)+(fibo-2)
# (fn)=(fn-1)+(fn-2)


# Esercizio 3 — Un po' più impegnativo (ricorsione su una struttura dati)
# Scrivi una funzione ricorsiva somma_lista(lista) che somma tutti i numeri di una lista Python (es. somma_lista([3, 7, 2, 5]) deve dare 17), senza usare sum()
# già pronta, e senza usare un ciclo for — solo ricorsione pura. Indizio: il caso base qui non è un numero come 0, ma una situazione diversa — 
# quale lista è "già la più semplice possibile, senza bisogno di scomporla ulteriormente"?
def somma_lista(lista):
    if lista == []:              # caso base: lista vuota
        return 0                  # neutro dell'addizione
    return lista[0] + somma_lista(lista[1:])   # primo elemento + somma del resto
print(somma_lista([3, 7, 2, 5]))

# 🟢 Esercizio 1 — Somma da 1 a N

# Scrivi una funzione ricorsiva:

# def somma(n):
#     ...

# che restituisca la somma di tutti i numeri da 1 a n.

# Esempio:

# somma(5) → 15

# perché:

# 5 + 4 + 3 + 2 + 1 = 15

# Vincolo: non usare for o while.

def somma(n):
    if n == 0:
        return 0
    return somma(n-1) 

# 🟡 Esercizio 2 — Potenza

# Scrivi una funzione ricorsiva:

# def potenza(base, esponente):
#     ...

# che calcoli base elevato a esponente.

# Esempi:

# potenza(2, 3) → 8
# potenza(5, 2) → 25
# potenza(10, 0) → 1

# Suggerimento: ragiona sulla relazione:

# 2³ = 2 × 2²
# 2² = 2 × 2¹
# 2¹ = 2 × 2⁰

# Quindi devi individuare il caso base e il modo in cui l'esponente si avvicina a quel caso.

def potenza(base, esponente):

    # CASO BASE
    if esponente == 0:
        return 1

    # PASSO RICORSIVO
    return base * potenza(base, esponente - 1)
print(potenza(4,3))

# eseguo la prima chiamata

# 3 è uguale a 0? no

# esco dall'if e vado al return della funzione

# eseguo il calcolo: 4 × potenza(4, 3-1)

# potenza(4,2)

# seconda chiamata

# 2 è uguale a 0? no

# esco dall'if e vado al return della funzione

# eseguo il calcolo: 4 × potenza(4, 2-1)

# potenza(4,1)

# terza chiamata

# 1 è uguale a 0? no

# esco dall'if e vado al return della funzione

# eseguo il calcolo: 4 × potenza(4, 1-1)

# potenza(4,0)

# quarta chiamata

# 0 è uguale a 0? sì

# ritorna 1

# calcolo ogni chiamata della funzione

# potenza(4,3)
# 4 × potenza(4,2)

# potenza(4,2)
# 4 × potenza(4,1)

# potenza(4,1)
# 4 × potenza(4,0)

# potenza(4,0)
# ritorna 1

# quindi:

# 4 × 4 × 4 × 1 = 64