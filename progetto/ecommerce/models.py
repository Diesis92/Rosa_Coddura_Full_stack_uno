from django.db import models

class Prodotto(models.Model):
    nome=models.CharField(max_length=100)
    descrizione= models.TextField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True, blank=True)
    prezzo=models.DecimalField(max_digits=8,decimal_places=2)
    quantita_disponibile=models.PositiveBigIntegerField()

    def __str__(self):
        return self.nome
    #estendi

    class Meta:
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"
        ordering = ['nome']

class Categoria(models.Model):
    nome=models.CharField(max_length=100)


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"
        ordering = ['nome']

    
