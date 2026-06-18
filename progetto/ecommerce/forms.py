from django import forms
from .models import Prodotto


class AcquistoForm(forms.Form):
    prodotto = forms.ModelChoiceField(queryset=Prodotto.objects.all())
    quantita = forms.IntegerField(min_value=1)
    codice_sconto = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        quantita = cleaned_data.get('quantita')
        prodotto = cleaned_data.get('prodotto')

        if quantita is not None and prodotto is not None:
            if quantita > prodotto.quantita_disponibile:
                raise forms.ValidationError(
                    "La quantità selezionata non è disponibile"
                )

        return cleaned_data

    def clean_quantita(self):
        quantita = self.cleaned_data.get('quantita')

        if quantita is not None and quantita <= 0:
            raise forms.ValidationError(
                "La quantità deve essere maggiore di zero"
            )

        return quantita
    #clean quantità minima di prodotti per sconto
    def clean_codice_sconto(self):
        codice = self.cleaned_data.get('codice_sconto')

        codici_validi = [
            'TIPIACEVINCEREFACILE',
            'WELCOME',
            'PALERMO',
            'TUVUOIFAREILPOVERACCIO'
        ]

        if codice and codice not in codici_validi:
            raise forms.ValidationError("Codice non valido")

        return codice