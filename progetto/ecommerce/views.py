from django.shortcuts import render
from .forms import AcquistoForm
from .models import Prodotto

def acquisto_prodotto(request):
    if request.method == 'POST':
        form = AcquistoForm(request.POST)
        if form.is_valid():
            prodotto_selezionato = form.cleaned_data['prodotto']
            quantita_desiderata = form.cleaned_data['quantita']
            codice_sconto= form.cleaned_data['codice_sconto']
            prezzo_unitario = prodotto_selezionato.prezzo
            prezzo_totale = prezzo_unitario * quantita_desiderata


            #calcolo sconto
            if codice_sconto:
                sconto_applicato = prezzo_totale * 0.25
                prezzo_totale -= sconto_applicato
            else:
                sconto_applicato = 0

            prezzo_totale += prezzo_totale * 0.22

            return render(request, 'conferma_acquisto.html', {
                'prodotto': prodotto_selezionato,
                'quantita': quantita_desiderata,
                'prezzo_totale': prezzo_totale,
                'sconto': sconto_applicato
            })

    else:
        form = AcquistoForm()

    return render(request, 'acquisto_prodotto.html', {'form': form})

