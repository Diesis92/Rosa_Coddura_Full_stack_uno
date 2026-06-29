from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"
        ordering = ["nome"]


class Tag(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Prodotto(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    tags = models.ManyToManyField(Tag, blank=True)

    prezzo = models.DecimalField(max_digits=8, decimal_places=2)
    quantita_disponibile = models.PositiveBigIntegerField()

    # ✔ sconto prodotto (percentuale)
    sconto_percentuale = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        categoria = self.categoria.nome if self.categoria else "Senza categoria"
        return f"{self.nome} | €{self.prezzo} | {categoria}"

    class Meta:
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"
        ordering = ["nome"]