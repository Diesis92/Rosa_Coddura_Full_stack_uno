from django.db import models


class Categoria(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome categoria"
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Prodotto(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome prodotto"
    )

    prezzo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prezzo (€)"
    )

    in_stock = models.BooleanField(
        default=True,
        verbose_name="Disponibile"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='prodotti',
        verbose_name="Categoria"
    )

    class Meta:
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"
        ordering = ['prezzo']

    def __str__(self):
        return f"{self.nome} — {self.prezzo}€"


class Ordine(models.Model):

    prodotti = models.ManyToManyField(
        Prodotto,
        through='OrdineProdotto',
        related_name='ordini',
        verbose_name="Prodotti"
    )

    data = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data ordine"
    )

    class Meta:
        verbose_name = "Ordine"
        verbose_name_plural = "Ordini"
        ordering = ['-data']

    def __str__(self):
        return f"Ordine #{self.id}"


class OrdineProdotto(models.Model):

    ordine = models.ForeignKey(
        Ordine,
        on_delete=models.CASCADE
    )

    prodotto = models.ForeignKey(
        Prodotto,
        on_delete=models.CASCADE
    )

    quantita = models.PositiveIntegerField(
        default=1,
        verbose_name="Quantità"
    )

    class Meta:
        verbose_name = "Ordine Prodotto"
        verbose_name_plural = "Ordini Prodotti"

    def __str__(self):
        return f"{self.ordine} - {self.prodotto} x {self.quantita}"