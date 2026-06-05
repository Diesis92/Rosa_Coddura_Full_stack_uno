from django.db import models


class Artista(models.Model):
    nome = models.CharField(max_length=150)
    nazionalita = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)
    data_debutto = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.nazionalita or 'N/A'}) - Album: {self.albums.count()}"

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artisti"
        ordering = ['nome']


class Album(models.Model):
    titolo = models.CharField(max_length=200)
    artista = models.ForeignKey(
        Artista,
        on_delete=models.PROTECT,
        related_name='albums'
    )
    anno = models.IntegerField(null=True, blank=True, verbose_name="Anno")

    GENERE_CHOICES = [
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Jazz', 'Jazz'),
        ('Classica', 'Classica'),
        ('Altro', 'Altro'),
    ]

    genere = models.CharField(
        max_length=10,
        choices=GENERE_CHOICES,
        default='Altro',
        verbose_name="Genere"
    )

    disponibile = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titolo} - {self.artista.nome} - {self.anno} - {self.genere}"

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Album"
        ordering = ['-anno']


class Canzone(models.Model):
    titolo = models.CharField(max_length=200)

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
        return f"{self.titolo} - {self.album.titolo} - {self.durata_secondi}s - traccia {self.traccia}"

    class Meta:
        verbose_name = "Canzone"
        verbose_name_plural = "Canzoni"
        ordering = ['traccia']


class ProfiloArtista(models.Model):
    artista = models.OneToOneField(
        Artista,
        on_delete=models.CASCADE,
        related_name='profilo'
    )
    dettagli = models.TextField(blank=True)

    def __str__(self):
        return f"Profilo di {self.artista.nome}"

    class Meta:
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


class Commento(models.Model):
    canzone = models.ForeignKey(
        Canzone,
        on_delete=models.CASCADE,
        related_name='commenti'
    )
    testo = models.TextField()
    autore = models.CharField(max_length=100)
    data_pubblicazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autore} - {self.canzone.titolo}: {self.testo[:50]}"

    class Meta:
        verbose_name = "Commento"
        verbose_name_plural = "Commenti"
        ordering = ['-data_pubblicazione']