from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Artista, Album, Canzone


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nazionalita', 'data_debutto')
    search_fields = ('nome', 'nazionalita')
    ordering = ('nome',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'artista', 'anno', 'genere')
    list_filter = ('genere', 'anno')
    search_fields = ('titolo', 'artista__nome')
    ordering = ('anno',)


@admin.register(Canzone)
class CanzoneAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'album', 'traccia', 'durata_secondi')
    list_filter = ('album',)
    search_fields = ('titolo', 'album__titolo')
    ordering = ('traccia',)
