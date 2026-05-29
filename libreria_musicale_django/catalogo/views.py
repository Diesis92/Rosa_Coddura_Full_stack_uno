from django.http import ( #fvb
    HttpResponse,
    JsonResponse,
    HttpResponseNotAllowed,
    HttpResponseBadRequest,
    HttpResponseRedirect
)

from .models import Artista, Album


def home(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return HttpResponse("<h1>Benvenuto nella Libreria Musicale</h1>")


def artista_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    artisti = Artista.objects.all()

    data = []
    for artista in artisti:
        data.append({
            'id': artista.id,
            'nome': artista.nome
        })

    return JsonResponse(data, safe=False)


def album_list(request): #togliere la logica for perché è una cosa che si mette sul template. Qua non serve la logica
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    albums = Album.objects.all()

    data = []
    for album in albums:
        data.append({
            'id': album.id,
            'titolo': album.titolo,
            'anno': album.anno
        })

    return JsonResponse(data, safe=False)

def album_detail(request, album_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        return HttpResponseBadRequest("Album non trovato")

    return JsonResponse({
        'id': album.id,
        'titolo': album.titolo,
        'artista': album.artista.nome,
        'anno': album.anno
    })


def redirect_home(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    return HttpResponseRedirect('/catalogo/')