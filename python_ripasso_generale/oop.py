#classe
#attribuiti di classe
#costruttore init
#attributi di istanza
#metodi
#creazioni istanze
#print ogetti

# class Automobile:
#     """Rappresenta un'automobile generica."""
#     # Attributo di classe (condiviso da tutte le istanze)
#     categoria = "veicolo a motore"
#     def __init__(self, marca, modello, colore):
#         # Attributi di istanza (unici per ogni oggetto)
#         self.marca = marca
#         self.modello = modello
#         self.colore = colore
#         self.velocita = 0
#     def accelera(self, incremento):
#         """Aumenta la velocità dell'automobile."""
#         self.velocita += incremento
#         return f"{self.marca} ora va a {self.velocita} km/h"
#     def descrizione(self):
#         """Restituisce una descrizione dell'auto."""
#         return f"{self.colore} {self.marca} {self.modello}"
# Creazione di istanze (oggetti)
# auto1 = Automobile("Fiat", "Panda", "rossa")
# auto2 = Automobile("Tesla", "Model 3", "nera")
# print(auto1.descrizione())   # rossa Fiat Panda
# print(auto2.accelera(100))   # Tesla ora va a 100 km/h
# print(auto1.categoria)       # veicolo a motores

# class SquadraCalcio:

#     def __init__(self, nome, citta, numero_giocatori):

#         self.nome = nome
#         self.citta = citta

        # Valore fisso: ogni squadra avrà sempre 20 giocatori
        # self.numero_giocatori = 20


# squadra1 = SquadraCalcio("Palermo", "Palermo", 20)

# print(squadra1.nome)
# print(squadra1.citta)
# print(squadra1.numero_giocatori)

# class SquadraCalcio:

#     def __init__(self, nome, citta, numero_giocatori=20):

#         self.nome = nome
#         self.citta = citta

#         # 20 è il valore predefinito,
#         # ma può essere modificato quando creo l'oggetto
#         self.numero_giocatori = numero_giocatori


# squadra1 = SquadraCalcio("Palermo", "Palermo")

# squadra2 = SquadraCalcio("Roma", "Roma", 25)

# print(squadra1.numero_giocatori)  # 20
# print(squadra2.numero_giocatori)  # 25


class Chitarra:
    def __init__(self, modello, marca, numero_corde=6):
        self.modello=modello
        self.marca=marca
        self.numero_corde= numero_corde

    def __str__(self):
        return f"{self.marca} {self.modello} - {self.numero_corde} corde"

c1=Chitarra("Stratocaster", "Fender")
c2=Chitarra("Telecaster 7-String", "Fender",7)
print(c1)
print(c2)





        
