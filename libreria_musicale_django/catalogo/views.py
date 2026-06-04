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
#applicare il decoratore @login_required alle view che richiedono autenticazione, ad esempio:


from django.http import (
    HttpResponse,
    JsonResponse,
    HttpResponseRedirect,
    HttpResponseNotAllowed,
)

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from functools import wraps

from asgiref.sync import iscoroutinefunction

from django.middleware.cache import CacheMiddleware
from django.utils.cache import add_never_cache_headers, patch_cache_control
from django.utils.decorators import decorator_from_middleware_with_args
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from .models import Commento
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
    


#esercizio 1: Proteggi una view
@login_required(login_url='/accounts/login/')
def profilo_utente(request):
    # mostra il profilo dell'utente autenticato
    context = {
        'utente': request.user
    }
    return render(request, 'catalogo/profilo.html', context)

#esercizio 2 cache
@cache_page(60 * 15, key_prefix='homepage')  # Mette in cache la pagina per 15 minuti
def homepage(request):
    return render(request, 'catalogo/homepage.html')

#esercizio 3 metodi HTTP con endpoint sicuro che accetta solo POST per eliminare un commento
@require_POST
def elimina_commento(request, commento_id):
    commento = get_object_or_404(Commento, id=commento_id)
    commento.delete()
    return JsonResponse({'status': 'success'})

#esercizio 4 CBV con method decorator dashboard protetta da login_required

@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
@method_decorator(login_required, name='dispatch')
class ReportView(View):

    def get(self, request):
        return render(request, 'report.html')

    def post(self, request):
        return render(request, 'report.html', {
            'message': 'POST ricevuto'
        })