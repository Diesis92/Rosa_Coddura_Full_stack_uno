# # shop/models.py

# from django.db import models

# class Prodotto(models.Model):
#     nome = models.CharField(max_length=100)
#     prezzo = models.DecimalField(max_digits=6, decimal_places=2)
#     disponibile = models.BooleanField(default=True)

#model sbagliato

from django.db import models

class Prodotto(models.Model):
    nome = models.CharField(max_length=100)
    prezzo = models.DecimalField(max_digits=6, decimal_places=2)

    def prezzo_scontato(self):
        return prezzo * 0.8   # ❌ ERRORE