from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from decimal import Decimal, ROUND_HALF_UP

from .models import Prodotto, Categoria
from .forms import AcquistoForm


# =========================
# CATALOGO (CBV)
# =========================
class CatalogoProdottiView(ListView):
    model = Prodotto
    template_name = "ecommerce/catalogo.html"
    context_object_name = "prodotti"

    def get_queryset(self):
        queryset = Prodotto.objects.all()

        categoria_id = self.request.GET.get("categoria")
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)

        disponibili = self.request.GET.get("disponibili")
        if disponibili:
            queryset = queryset.filter(quantita_disponibile__gt=0)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorie"] = Categoria.objects.all()
        return context


# =========================
# DETAIL
# =========================
class ProdottoDetailView(DetailView):
    model = Prodotto
    template_name = "ecommerce/prodotto_detail.html"
    context_object_name = "prodotto"


# =========================
# CREATE
# =========================
class ProdottoCreateView(LoginRequiredMixin, CreateView):
    model = Prodotto
    fields = [
        "nome",
        "descrizione",
        "categoria",
        "tags",
        "prezzo",
        "quantita_disponibile",
        "sconto_percentuale"
    ]
    template_name = "ecommerce/prodotto_form.html"
    success_url = reverse_lazy("ecommerce:catalogo_prodotti")


# =========================
# UPDATE
# =========================
class ProdottoUpdateView(LoginRequiredMixin, UpdateView):
    model = Prodotto
    fields = [
        "nome",
        "descrizione",
        "categoria",
        "tags",
        "prezzo",
        "quantita_disponibile",
        "sconto_percentuale"
    ]
    template_name = "ecommerce/prodotto_form.html"
    success_url = reverse_lazy("ecommerce:catalogo_prodotti")


# =========================
# DELETE
# =========================
class ProdottoDeleteView(LoginRequiredMixin, DeleteView):
    model = Prodotto
    template_name = "ecommerce/prodotto_confirm_delete.html"
    success_url = reverse_lazy("ecommerce:catalogo_prodotti")


# =========================
# ACQUISTO (FBV)
# =========================
@login_required
def acquisto_prodotto(request):

    if request.method == "POST":
        form = AcquistoForm(request.POST)

        if form.is_valid():
            prodotto = form.cleaned_data["prodotto"]
            quantita = form.cleaned_data["quantita"]
            codice_sconto = form.cleaned_data["codice_sconto"]

            if prodotto.quantita_disponibile <= 0:
                form.add_error("prodotto", "Prodotto esaurito")
                return render(request, "ecommerce/acquisto_prodotto.html", {"form": form})

            # prezzo base
            prezzo_totale = prodotto.prezzo * quantita
            sconto = Decimal("0.00")

            # sconto prodotto
            if prodotto.sconto_percentuale > 0:
                sconto += prezzo_totale * (prodotto.sconto_percentuale / Decimal("100"))

            # sconto codice
            if codice_sconto:
                percentuale = AcquistoForm.CODICI_SCONTO[codice_sconto]
                sconto += prezzo_totale * (Decimal(percentuale) / Decimal("100"))

            # totale finale
            prezzo_totale -= sconto

            prezzo_totale = prezzo_totale.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            sconto = sconto.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

            # update stock
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

    return render(request, "ecommerce/acquisto_prodotto.html", {"form": form})


# =========================
# CONFERMA
# =========================
def conferma_acquisto(request):
    return render(request, "ecommerce/conferma_acquisto.html")


# =========================
# CATEGORIE (CBV)
# =========================
class CategoriaListView(ListView):
    model = Categoria
    template_name = "ecommerce/categorie.html"
    context_object_name = "categorie"