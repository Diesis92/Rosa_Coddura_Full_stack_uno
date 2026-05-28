from django.db import models

# Create your models here.
class Artista(models.Model):
    nome = models.TextField(max_length=150)
    nazionalita = models.TextField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)
    data_debutto = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome} ({self.nazionalita}) - Album: {self.albums.count()}"
    

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artisti"
        ordering = ['nome']
    
class Album(models.Model):
    titolo = models.TextField(max_length=200)
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT, related_name='albums') # related_name='albums': permette di accedere agli album di un artista con artista.albums.all()
    anno = models.IntegerField(null=True, blank=True, verbose_name="Anno")
    GENERE_CHOICES = [
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Jazz', 'Jazz'),
        ('Classica', 'Classica'),
        ('Altro', 'Altro'),
    ]
    genere = models.CharField(max_length=10, choices=GENERE_CHOICES, default='Altro', verbose_name="Genere")
    disponibile = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.titolo} - {self.artista.nome} - {self.anno} - {self.genere}"

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Album"
        ordering = ['anno']

class Canzone(models.Model):
    titolo = models.TextField(max_length=200)

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='canzoni'
    )

    durata_secondi = models.IntegerField(verbose_name="Durata in secondi")
    traccia = models.IntegerField(verbose_name="Numero di traccia")

    tags = models.ManyToManyField(
        'Tag',
        related_name='canzoni',
        blank=True
    )

    def __str__(self):
        return f"{self.titolo} - {self.album.titolo} - {self.durata_secondi} secondi - traccia {self.traccia}"

    class Meta:
        verbose_name = "Canzone"
        verbose_name_plural = "Canzoni"
        ordering = ['traccia']
    

    #ManyTo Many: Un artista può avere più album, ma un album appartiene a un solo artista. Un album può avere più canzoni, ma una canzone appartiene a un solo album.

    #Modello tag - canzone ManyToMany: Se si volesse aggiungere un modello Tag per categorizzare le canzoni, si potrebbe creare una relazione ManyToMany tra Canzone e Tag, poiché una canzone può avere più tag e un tag può essere associato a più canzoni.
    #OneToOne un artista ha un profilo dettagliato: Se si volesse aggiungere un modello ProfiloArtista per memorizzare informazioni dettagliate su un artista, si potrebbe creare una relazione OneToOne tra Artista e ProfiloArtista, poiché ogni artista avrebbe un solo profilo dettagliato e ogni profilo sarebbe associato a un solo artista.

class ProfiloArtista(models.Model):
    artista = models.OneToOneField(Artista, on_delete=models.CASCADE, related_name='profilo') #il nome è meglio che sia esteso tra le due relazioni, così è più chiaro quando si accede al profilo di un artista con artista.profilo
    dettagli = models.TextField(blank=True)

    def __str__(self):
        return f"Profilo di {self.artista.nome} - Dettagli: {self.dettagli[:50]}..."

    class Meta:                              # ✅ dentro ProfiloArtista
        verbose_name = "Profilo Artista"
        verbose_name_plural = "Profili Artisti"
        ordering = ['artista__nome']


class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['nome']



# OneToOne  → un Artista ha UN solo ProfiloArtista
# OneToMany → un Artista ha MOLTI Album (ForeignKey)
# ManyToMany→ un Album può avere MOLTI Tag, un Tag può stare su MOLTI Album

# 1.	Artista:nome (testo,max 150 car.) nazionalita(testo,max 100 car., opzionale), biografia(testo lungo opzionale), data_debutto(data, opzionale)
# 2.	Album: titolo(testo, max 200 car.), artista(ForeignKey: un album ha un solo artista, proteggere l’artista dalla cancellazione), anno(intero), genere(choices: Rock/Pop/Jazz/Classica/Altro, ci vorrebbe un altro modello però)
# 3.	Canzone:titolo (testo, max 200 car.), album(ForeignKey con cancellazione a cascata), durata_secondi(intero), traccia(intero—numero di traccia nell’album)
# 4.	Tutti e tre: metodo__str__ significativo e classe Meta con ordinamento appropriato

