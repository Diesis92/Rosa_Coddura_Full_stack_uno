from django.db import models

# Create your models here usando ORM di Django per definire la struttura del database per i prodotti del catalogo
class Prodotto(models.Model):
    nome = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    disponibile = models.BooleanField(default=True)
    creato_il = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    class Meta: #Metadati per il modello Prodotto, ad esempio per definire l'ordinamento predefinito
        ordering = ['-creato_il'] #asc e desc per ordinare i prodotti in base alla data di creazione, dal più recente al più vecchio
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"
