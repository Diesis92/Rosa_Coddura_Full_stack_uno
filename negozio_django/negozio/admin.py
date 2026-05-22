from django.contrib import admin
from .models import Categoria, Prodotto, Ordine, OrdineProdotto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(Prodotto)
class ProdottoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'prezzo', 'in_stock', 'categoria')
    list_filter = ('in_stock', 'categoria')
    search_fields = ('nome',)


class OrdineProdottoInline(admin.TabularInline):
    model = OrdineProdotto
    extra = 1


@admin.register(Ordine)
class OrdineAdmin(admin.ModelAdmin):
    list_display = ('id', 'data')
    inlines = [OrdineProdottoInline]


@admin.register(OrdineProdotto)
class OrdineProdottoAdmin(admin.ModelAdmin):
    list_display = ('ordine', 'prodotto', 'quantita')