class SquadraCalcio:
    def __init__(self, nome, numero_giocatori=11):
        self.nome=nome
        self.numero_giocatori=numero_giocatori
    def __str__(self):
         return f"Squadra: {self.nome}, Giocatori: {self.numero_giocatori}"
    def __repr__(self):
         return f"SquadraCalcio('{self.nome}', {self.numero_giocatori})"
    def __len__(self):
         return self.numero_giocatori

squadra = SquadraCalcio("Palermo")
print(repr(squadra))
print(len(squadra))
print(squadra)

