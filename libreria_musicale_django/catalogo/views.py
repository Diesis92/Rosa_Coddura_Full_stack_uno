# # ── django.http ────────────────────────────────────────────────────────────────
# from django.http import (
#     HttpResponse,           # risposta HTML grezza — 200
#     JsonResponse,           # risposta JSON — 200
#     HttpResponseRedirect,   # reindirizzamento — 302
#     HttpResponseBadRequest, # richiesta malformata — 400
#     HttpResponseNotFound,   # risorsa non trovata — 404
#     HttpResponseNotAllowed, # metodo HTTP non permesso — 405
#     HttpResponseServerError # errore interno — 500
# )

# # ── django.shortcuts ───────────────────────────────────────────────────────────
# from django.shortcuts import (
#     render,              # renderizza un template HTML
#     redirect,            # reindirizza a un URL o a un name
#     get_object_or_404,   # get() + 404 automatico se non esiste
#     get_list_or_404      # filter() + 404 automatico se lista vuota
# )

# # ── django.views ───────────────────────────────────────────────────────────────
# from django.views import View                    # CBV base

# # ── django.views.generic ───────────────────────────────────────────────────────
# from django.views.generic import (
#     ListView,    # lista oggetti
#     DetailView,  # dettaglio singolo oggetto
#     CreateView,  # form creazione
#     UpdateView,  # form modifica
#     DeleteView   # form cancellazione
# )

# # ── django.views.decorators.http ───────────────────────────────────────────────
# from django.views.decorators.http import (
#     require_http_methods,  # @require_http_methods(["GET", "POST"])
#     require_GET,           # solo GET
#     require_POST           # solo POST
# )

# # ── models ─────────────────────────────────────────────────────────────────────
# from .models import Artista, Album, Canzone


# def home(request):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])
#     return HttpResponse("<h1>Benvenuto nella Libreria Musicale</h1>")


# def artista_list(request):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])

#     artisti = Artista.objects.all()

#     data = []
#     for artista in artisti:
#         data.append({
#             'id': artista.id,
#             'nome': artista.nome
#         })

#     return JsonResponse(data, safe=False)


# def album_list(request): #togliere la logica for perché è una cosa che si mette sul template. Qua non serve la logica
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])

#     albums = Album.objects.all()

#     data = []
#     for album in albums:
#         data.append({
#             'id': album.id,
#             'titolo': album.titolo,
#             'artista': album.artista.nome,
#             'anno': album.anno
#         })
#     return JsonResponse(data, safe=False)
    
# #CBV 
# # class AlbumListView(View):
# #     def get(self, request):
# #         albums = Album.objects.all()

# #        context = {
# #             'albums': albums
# #         }
# #        return render(request, 'album_list.html', context)

# class AlbumListView(View):
#     def get(self, request):
#         albums = Album.objects.all()
#         context = {
#             'albums': albums
#         }
#         return render(request, 'album_list.html', context)

# def album_detail(request, album_id):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])

#     try:
#         album = Album.objects.get(id=album_id)
#     except Album.DoesNotExist:
#         return HttpResponseBadRequest("Album non trovato")

#     return JsonResponse({
#         'id': album.id,
#         'titolo': album.titolo,
#         'artista': album.artista.nome,
#         'anno': album.anno
#     })


# def redirect_home(request):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])

#     return HttpResponseRedirect('/catalogo/')


# ----------------------------------------------------------------------------------

from django.http import (
    HttpResponse,
    JsonResponse,
    HttpResponseRedirect,
    HttpResponseNotAllowed,
)
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Artista, Album, Canzone


def home(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return HttpResponse("<h1>Benvenuto nella Libreria Musicale</h1>")


def artista_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    artisti = Artista.objects.all()
    data = [{'id': a.id, 'nome': a.nome} for a in artisti]
    return JsonResponse(data, safe=False)


def album_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    albums = Album.objects.all()
    data = [{'id': a.id, 'titolo': a.titolo,
             'artista': a.artista.nome, 'anno': a.anno}
            for a in albums]
    return JsonResponse(data, safe=False)


def album_detail(request, album_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    album = get_object_or_404(Album, id=album_id)
    return JsonResponse({
        'id': album.id,
        'titolo': album.titolo,
        'artista': album.artista.nome,
        'anno': album.anno,
    })


def redirect_home(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return HttpResponseRedirect('/catalogo/')


class AlbumListView(View):
    def get(self, request):
        albums = Album.objects.all()
        context = {'albums': albums}
        return render(request, 'catalogo/album_list.html', context)
    
#DetailView
class AlbumDetailView(View):
    def get(self, request, pk):
        album = get_object_or_404(Album, id=pk)
        return render(request, 'catalogo/album_detail.html', {
            'album': album
        })