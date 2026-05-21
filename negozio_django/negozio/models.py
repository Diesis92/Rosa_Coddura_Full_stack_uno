from django.db import models

# Create your models here.
class categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome    

class meta(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class prodotto(models.Model):
    nome = models.CharField(max_length=100)
    prezzo = models.FloatField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    meta = models.ForeignKey(meta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome    
    
