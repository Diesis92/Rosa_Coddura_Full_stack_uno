from django import forms
from .models import Prodotto


class AcquistoForm(forms.Form):
    prodotto = forms.ModelChoiceField(queryset=Prodotto.objects.all())
    quantita = forms.IntegerField(min_value=1)
    codice_sconto = forms.CharField(required=False)

    # ✔ mappa sconti codice → percentuale
    CODICI_SCONTO = {
        "WELCOME": 10,
        "TIPIACEVINCEREFACILE": 25,
        "PALERMO": 15,
        "TUVUOIFAREILPOVERACCIO": 50
    }

    def clean(self):
        cleaned_data = super().clean()

        prodotto = cleaned_data.get("prodotto")
        quantita = cleaned_data.get("quantita")

        if prodotto and quantita:
            if quantita > prodotto.quantita_disponibile:
                raise forms.ValidationError("Quantità non disponibile")

        return cleaned_data

    def clean_codice_sconto(self):
        codice = self.cleaned_data.get("codice_sconto")

        if codice and codice not in self.CODICI_SCONTO:
            raise forms.ValidationError("Codice non valido")

        return codice