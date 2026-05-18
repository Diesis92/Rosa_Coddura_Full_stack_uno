from django.contrib import admin

# Register your models here.
from .models import Prodotto

@admin.register(Prodotto)
class ProdottoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'prezzo', 'disponibile', 'creato_il'] #campi da visualizzare nella lista dei prodotti nell'admin
    list_filter = ['disponibile'] #filtri per la disponibilità e la data di creazione
    search_fields = ['nome', 'descrizione'] #campi su cui effettuare la ricerca rapida nell'admin
    list_editable = ['disponibile', 'prezzo'] #campi modificabili direttamente dalla lista dei prodotti nell'admin