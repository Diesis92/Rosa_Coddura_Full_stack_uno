from django.db import models

# Create your models here.
class Autore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} {self.cognome}"
    
class Meta:
    verbose_name_plural = "Autori"
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
class Meta:
    verbose_name_plural = "Categorie"
    
class Libro(models.Model):
    titolo = models.CharField(max_length=200)

    autore = models.ForeignKey(
        Autore,
        on_delete=models.CASCADE
    )

    categorie = models.ManyToManyField(Categoria)

    anno_pubblicazione = models.IntegerField()

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Libri"