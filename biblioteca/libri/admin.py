from django.contrib import admin
from .models import Autore, Categoria, Libro


class AutoreAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome')
    list_filter = ('nome', 'cognome')
    search_fields = ('nome', 'cognome')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'autore', 'anno_pubblicazione')
    list_filter = ('autore', 'categorie')
    search_fields = ('titolo',)
    filter_horizontal = ('categorie',)


admin.site.register(Autore, AutoreAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Libro, LibroAdmin)