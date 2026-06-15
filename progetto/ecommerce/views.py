from django.shortcuts import render
from decimal import Decimal
from .models import Prodotto
from .forms import AcquistoForm


def acquisto_prodotto(request):
    if request.method == "POST":
        form = AcquistoForm(request.POST)

        if form.is_valid():
            prodotto = form.cleaned_data["prodotto"]
            quantita = form.cleaned_data["quantita"]
            codice_sconto = form.cleaned_data["codice_sconto"]

            prezzo_totale = prodotto.prezzo * quantita

            sconto = Decimal("0.00")

            if codice_sconto:
                sconto = prezzo_totale * Decimal("0.25")
                prezzo_totale -= sconto

            prezzo_totale += prezzo_totale * Decimal("0.22")

            # NON fare redirect: usiamo render diretto
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
    # opzionale: se qualcuno entra direttamente
    return render(request, "ecommerce/conferma_acquisto.html")


def catalogo_prodotti(request):
    prodotti = Prodotto.objects.all()

    return render(request, "ecommerce/catalogo.html", {
        "prodotti": prodotti
    })