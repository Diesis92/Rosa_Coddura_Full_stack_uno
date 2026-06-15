from django.db import models

class Prodotto(models.Model):
    nome=models.CharField(max_length=100)
    descrizione= models.TextField()
    prezzo=models.DecimalField(max_digits=8,decimal_places=2)
    quantita_disponibile=models.PositiveBigIntegerField()

    def __str__(self):
        return self.nome


class Meta:
    verbose_name = "Prodotto"
    verbose_name_plural = "Prodotti"
    ordering = ['nome']
