# def decoratore(funzione):
#     def wrapper():
#         print("vorrei aggiungere una stella")
#         funzione()
#         print("ho aggiunto una stella")
#     return wrapper

# @decoratore
# def albero():
#     print("io sono un albero")

# albero()


import time


def tempo(funzione):
    def wrapper():
        tempo_inizio=time.time()
        funzione()
        tempo_fine = time.time()
        print(tempo_fine-tempo_inizio)
    return wrapper
@tempo
def esempio():
    print("sto facendo qualcosa")

esempio()
# IMPORTA modulo time


# DEFINISCI funzione decoratore(funzione_originale)

#     DEFINISCI funzione wrapper()

#         SALVA tempo_inizio = time.ora_attuale()

#         ESEGUI funzione_originale()

#         SALVA tempo_fine = time.ora_attuale()

#         STAMPA (tempo_fine - tempo_inizio)

#     RESTITUISCI wrapper


# USA decoratore su una funzione

#     @decoratore
#     DEFINISCI funzione esempio()

#         STAMPA "sto facendo qualcosa"


# CHIAMO esempio()