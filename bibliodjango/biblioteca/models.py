from django.db import models

class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.CharField(max_length=100)
    anno_pubblicazione = models.DateField()
    disponibile = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titolo} di {self.autore} ({self.anno_pubblicazione}) - {'Disponibile' if self.disponibile else 'Non disponibile'}"

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"