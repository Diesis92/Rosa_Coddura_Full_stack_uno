from django.contrib import admin
from .models import Prodotto

@admin.register(Prodotto)
class ProdottoAdmin(admin.ModelAdmin):
    list_display=("nome","descrizione","prezzo","quantita_disponibile")
    search_fields =("nome", "prezzo", "quantita_disponibile"),
    ordering=("nome","descrizione","prezzo","quantita_disponibile")


