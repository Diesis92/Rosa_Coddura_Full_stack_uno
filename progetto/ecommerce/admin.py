from django.contrib import admin
from .models import Prodotto, Categoria, Tag


@admin.register(Prodotto)
class ProdottoAdmin(admin.ModelAdmin):
    list_display = ("nome", "prezzo", "quantita_disponibile")
    search_fields = ("nome",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("nome",)