from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from decimal import Decimal, ROUND_HALF_UP

from .models import Prodotto, Categoria
from .forms import AcquistoForm


@login_required
def acquisto_prodotto(request):

    if request.method == "POST":
        form = AcquistoForm(request.POST)

        if form.is_valid():
            prodotto = form.cleaned_data["prodotto"]
            quantita = form.cleaned_data["quantita"]
            codice_sconto = form.cleaned_data["codice_sconto"]

            # Controllo prodotto esaurito
            if prodotto.quantita_disponibile == 0:
                form.add_error("prodotto", "Prodotto esaurito")

                return render(request, "ecommerce/acquisto_prodotto.html", {
                    "form": form
                })

            # Calcolo prezzo totale
            prezzo_totale = prodotto.prezzo * quantita

            # Applicazione sconto
            sconto = Decimal("0.00")

            if codice_sconto:
                sconto = prezzo_totale * Decimal("0.25")
                prezzo_totale -= sconto

            # Arrotondamento a due decimali (centesimi)
            prezzo_totale = prezzo_totale.quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_UP
            )

            sconto = sconto.quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_UP
            )

            # Aggiornamento quantità disponibile
            prodotto.quantita_disponibile -= quantita
            prodotto.save()

            return render(request, "ecommerce/conferma_acquisto.html", {
                "prodotto": prodotto,
                "quantita": quantita,
                "sconto": sconto,
                "prezzo_totale": prezzo_totale
            })

    else:
        form = AcquistoForm()

    return render(request, "ecommerce/acquisto_prodotto.html", {
        "form": form
    })


def conferma_acquisto(request):
    return render(request, "ecommerce/conferma_acquisto.html")


def catalogo_prodotti(request):
    prodotti = Prodotto.objects.all()

    return render(request, "ecommerce/catalogo.html", {
        "prodotti": prodotti
    })


def categoria_prodotti(request):
    categorie = Categoria.objects.all()

    return render(request, "ecommerce/categorie.html", {
        "categorie": categorie
    })