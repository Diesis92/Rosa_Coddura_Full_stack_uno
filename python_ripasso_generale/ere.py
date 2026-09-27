#class animale
#init
#metodo
#classe ereditata
#altra classe ereditata
#creazione istanze
#animale eredita 

# class Animale:
#     def __init__(self, nome):
#         self.nome= nome
#     def __str__(self):
#         return f"il mio nome è {self.nome}"
#     def __repr__(self):
#         return f"Cane(nome='{self.nome}')"
#     def presenta(self):
#         print(f"Ciao, il mio nome è {self.nome}")
# class Cane(Animale):
#     def abbaia(self):
#         print("woof!")
# class Gatto(Animale):
#     def miagola(self):
#         print("miao!")
# a1=Animale("Generico")
# c1=Cane("Bob")
# g1=Gatto("Micio")

# c1.presenta()
# g1.presenta()

# print(a1)
# print(c1)
# print(repr(c1))
# print(g1)

# print(isinstance(a1, Animale))
# print(isinstance(c1, Cane))
# print(isinstance(g1, Gatto))

class Animale:
    regno = "Animalia"
    def __init__(self,nome, specie,eta):
        self.nome=nome
        self.specie=specie
        self.eta=eta
        
    
        