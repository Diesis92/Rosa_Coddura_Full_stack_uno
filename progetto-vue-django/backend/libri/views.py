import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Libro

@csrf_exempt
def lista_libri(request):

    # GET → leggere libri

    if request.method == "GET":

        libri = Libro.objects.all()

        dati = []

        for libro in libri:
            dati.append({
                "id": libro.id,
                "titolo": libro.titolo,
                "autore": libro.autore
            })

        return JsonResponse(dati, safe=False)



    # POST 

    elif request.method == "POST":

        corpo = json.loads(request.body)


        nuovo_libro = Libro.objects.create(
            titolo=corpo["titolo"],
            autore=corpo["autore"]
        )


        return JsonResponse({
            "id": nuovo_libro.id,
            "titolo": nuovo_libro.titolo,
            "autore": nuovo_libro.autore
        }, status=201)

@csrf_exempt
def dettaglio_libro(request, id):

    libro = get_object_or_404(
        Libro,
        id=id
    )


    # GET → restituisce un singolo libro

    if request.method == "GET":

        return JsonResponse({
            "id": libro.id,
            "titolo": libro.titolo,
            "autore": libro.autore
        })


    # PUT → modifica completamente il libro

    elif request.method == "PUT":

        corpo = json.loads(request.body)

        libro.titolo = corpo["titolo"]
        libro.autore = corpo["autore"]

        libro.save()

        return JsonResponse({
            "id": libro.id,
            "titolo": libro.titolo,
            "autore": libro.autore
        })


    # PATCH → modifica solo i campi inviati

    elif request.method == "PATCH":

        corpo = json.loads(request.body)

        if "titolo" in corpo:
            libro.titolo = corpo["titolo"]

        if "autore" in corpo:
            libro.autore = corpo["autore"]

        libro.save()

        return JsonResponse({
            "id": libro.id,
            "titolo": libro.titolo,
            "autore": libro.autore
        })


    # DELETE → elimina il libro

    elif request.method == "DELETE":

        libro.delete()

        return JsonResponse({
            "messaggio": "Libro eliminato"
        })