from django import forms 
from .models import Prodotto

class AcquistoForm(forms.Form):
    prodotto = forms.ModelChoiceField(queryset=Prodotto.objects.all())
    quantita = forms.IntegerField(min_value=1)
    codice_sconto = forms.CharField(required=False)

    def clean(self):
        self.cleaned_data = super().clean()
        quantita = self.cleaned_data.get('quantita')
        prodotto = self.cleaned_data.get('prodotto')
        if quantita is not None and prodotto is not None:
            if quantita > prodotto.quantita_disponibile:
                raise forms.ValidationError(
                    "la quantità selezionata non è disponibile"
                )
        return self.cleaned_data
