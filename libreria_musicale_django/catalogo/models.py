from django.db import models

# Create your models here.
class Artista(models.Model):
    nome = models.TextField(max_length=150)
    nazionalita = models.TextField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)
    data_debutto = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.nome} - {self.nazionalita} - {self.biografia} - {self.data_debutto} - Album pubblicati: {self.albums.count()}"
    

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artisti"
        ordering = ['nome']
    
class Album(models.Model):
    titolo = models.TextField(max_length=200)
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT, related_name='albums')
    anno = models.IntegerField()
    GENERE_CHOICES = [
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Jazz', 'Jazz'),
        ('Classica', 'Classica'),
        ('Altro', 'Altro'),
    ]
    genere = models.CharField(max_length=10, choices=GENERE_CHOICES, default='Altro', verbose_name="Genere")

    def __str__(self):
        return f"{self.titolo} - {self.artista.nome} - {self.anno} - {self.genere}"

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Album"
        ordering = ['anno']

class Canzone(models.Model):
    titolo = models.TextField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canzoni')
    durata_secondi = models.IntegerField(verbose_name="Durata in secondi")
    traccia = models.IntegerField(verbose_name="Numero di traccia")

    def __str__(self):
        return f"{self.titolo} - {self.album.titolo} - {self.durata_secondi} secondi - traccia {self.traccia}"

    class Meta:
        verbose_name = "Canzone"
        verbose_name_plural = "Canzoni"
        ordering = ['traccia']
    

    


# 1.	Artista:nome (testo,max 150 car.) nazionalita(testo,max 100 car., opzionale), biografia(testo lungo opzionale), data_debutto(data, opzionale)
# 2.	Album: titolo(testo, max 200 car.), artista(ForeignKey: un album ha un solo artista, proteggere l’artista dalla cancellazione), anno(intero), genere(choices: Rock/Pop/Jazz/Classica/Altro, ci vorrebbe un altro modello però)
# 3.	Canzone:titolo (testo, max 200 car.), album(ForeignKey con cancellazione a cascata), durata_secondi(intero), traccia(intero—numero di traccia nell’album)
# 4.	Tutti e tre: metodo__str__ significativo e classe Meta con ordinamento appropriato

