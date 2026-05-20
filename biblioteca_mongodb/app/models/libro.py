class Libro:

    def __init__(self, titolo, autore, anno, genere, copie, disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.genere = genere
        self.copie = copie
        self.disponibili = disponibili

    def to_dict(self):
        return {
            "titolo": self.titolo,
            "autore": self.autore,
            "anno": self.anno,
            "genere": self.genere,
            "copie": self.copie,
            "disponibili": self.disponibili
        }