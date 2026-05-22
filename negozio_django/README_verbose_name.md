# Perché usare verbose_name sia nei campi che nella classe Meta?

Questa è una delle cose che genera più confusione in Django.
La risposta breve è: **sono due cose diverse che appaiono in posti diversi**.
Vediamo tutto nel dettaglio.

---

## Il problema senza verbose_name

Scrivi questo modello senza nessun verbose_name:

```python
class Prodotto(models.Model):
    nome      = models.CharField(max_length=200)
    prezzo    = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock  = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
```

Django apre il pannello admin e mostra questo:

```
NEGOZIO
  ├── Prodottos        ← aggiunge una "s" inglese al nome della classe
```

E dentro il form del singolo prodotto:

```
Nome      [_____________]    ← ok, questo è fortunato
Prezzo    [_____________]    ← ok
In stock  [ ]               ← toglie l'underscore ma in inglese
Categoria [_____________]    ← ok
```

Quindi Django fa del suo meglio — toglie gli underscore, mette la maiuscola —
ma sbaglia il plurale e lascia i nomi in inglese se la variabile è inglese.

---

## verbose_name nel campo — a cosa serve

Serve a dare un nome leggibile al **singolo campo** nel form dell'admin
(o in qualsiasi form Django generato automaticamente).

```python
class Prodotto(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome prodotto"      # ← etichetta del campo nel form
    )
    prezzo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prezzo (€)"         # ← etichetta del campo nel form
    )
    in_stock = models.BooleanField(
        default=True,
        verbose_name="Disponibile"        # ← etichetta del campo nel form
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        verbose_name="Categoria"          # ← etichetta del campo nel form
    )
```

Risultato nel form del singolo prodotto:

```
┌──────────────────────────────────────────────┐
│                                              │
│  Nome prodotto   [_________________________] │
│  Prezzo (€)      [_________________________] │
│  Disponibile     [ ]                         │
│  Categoria       [_________________________] │
│                                              │
└──────────────────────────────────────────────┘
```

Il `verbose_name` nel campo risponde alla domanda:
**"Come si chiama questa etichetta quando compilo il form?"**

---

## verbose_name nella classe Meta — a cosa serve

Serve a dare un nome leggibile al **modello intero** nel pannello admin —
sia il nome singolare che il plurale nel menu di navigazione.

```python
class Prodotto(models.Model):
    nome     = models.CharField(max_length=200)
    prezzo   = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name        = "Prodotto"    # ← nome singolare
        verbose_name_plural = "Prodotti"    # ← nome plurale nel menu
```

Risultato nel pannello admin:

```
NEGOZIO
  ├── Categorie     ← verbose_name_plural di Categoria
  ├── Prodotti      ← verbose_name_plural di Prodotto   ✅ non più "Prodottos"
  └── Ordini        ← verbose_name_plural di Ordine
```

E quando sei dentro la lista prodotti, Django usa il singolare nei messaggi:

```
Il Prodotto "Laptop" è stato aggiunto con successo.   ← verbose_name singolare
Seleziona il Prodotto da modificare.                  ← verbose_name singolare
```

Il `verbose_name` nella Meta risponde alla domanda:
**"Come si chiama questo modello nel menu e nei messaggi dell'admin?"**

---

## La differenza visiva — schema completo

```
Pannello Admin
│
├── Menu laterale
│     ├── NEGOZIO
│     │     ├── Prodotti   ← Meta.verbose_name_plural
│     │     ├── Categorie  ← Meta.verbose_name_plural
│     │     └── Ordini     ← Meta.verbose_name_plural
│
├── Lista oggetti
│     └── "Aggiungi Prodotto"   ← Meta.verbose_name (singolare)
│
└── Form del singolo oggetto
      ├── Nome prodotto   [___]   ← verbose_name del campo "nome"
      ├── Prezzo (€)      [___]   ← verbose_name del campo "prezzo"
      ├── Disponibile     [ ]     ← verbose_name del campo "in_stock"
      └── Categoria       [___]   ← verbose_name del campo "categoria"
```

---

## Sono obbligatori?

No, nessuno dei due è obbligatorio. Django funziona anche senza.
Ma ecco cosa succede se li ometti:

| Situazione | Senza verbose_name | Con verbose_name |
|---|---|---|
| Nome campo `in_stock` | "In stock" | "Disponibile" |
| Nome campo `prezzo` | "Prezzo" | "Prezzo (€)" |
| Plurale del modello | "Prodottos" | "Prodotti" |
| Singolare nei messaggi | "Prodotto" (ok per caso) | "Prodotto" |

Il `verbose_name` nel campo è più utile quando:
- Il nome della variabile è in inglese (`in_stock` → "Disponibile")
- Vuoi aggiungere unità di misura (`prezzo` → "Prezzo (€)")
- Il nome è ambiguo e vuoi chiarirlo

Il `verbose_name_plural` nella Meta è **quasi sempre necessario**
perché Django non conosce le regole del plurale italiano.

---

## Il modello completo con tutto spiegato

```python
from django.db import models


class Categoria(models.Model):

    # verbose_name nel campo:
    # → "Nome categoria" appare come etichetta nel form dell'admin
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome categoria"
    )

    class Meta:
        # verbose_name → usato nei messaggi singolari dell'admin
        # es. "La Categoria è stata aggiunta con successo"
        verbose_name = "Categoria"

        # verbose_name_plural → usato nel menu laterale dell'admin
        # senza questo Django scriverebbe "Categorias"
        verbose_name_plural = "Categorie"

        # ordering → ordine di default quando recuperi le categorie
        # equivale a ORDER BY nome ASC in SQL
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Prodotto(models.Model):

    # verbose_name "Nome prodotto" → etichetta nel form
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome prodotto"
    )

    # verbose_name "Prezzo (€)" → aggiunge l'unità di misura all'etichetta
    # senza verbose_name il campo si chiamerebbe solo "Prezzo"
    prezzo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prezzo (€)"
    )

    # verbose_name "Disponibile" → traduce il nome inglese in_stock
    # senza verbose_name il campo si chiamerebbe "In stock" (con spazio)
    in_stock = models.BooleanField(
        default=True,
        verbose_name="Disponibile"
    )

    # verbose_name "Categoria" → etichetta del campo ForeignKey nel form
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='prodotti',
        verbose_name="Categoria"
    )

    class Meta:
        # verbose_name → "Il Prodotto è stato salvato con successo"
        verbose_name = "Prodotto"

        # verbose_name_plural → voce nel menu dell'admin
        # senza questo Django scriverebbe "Prodottos"
        verbose_name_plural = "Prodotti"

        # ordering → i prodotti sono ordinati per prezzo crescente di default
        # ogni volta che fai Prodotto.objects.all() li ricevi già ordinati
        ordering = ['prezzo']

    def __str__(self):
        return f"{self.nome} — {self.prezzo}€"


class Ordine(models.Model):

    # verbose_name "Prodotto" → etichetta del campo ForeignKey nel form
    prodotto = models.ForeignKey(
        Prodotto,
        on_delete=models.CASCADE,
        related_name='ordini',
        verbose_name="Prodotto"
    )

    # verbose_name "Quantità" → aggiunge l'accento che il nome variabile non ha
    # senza verbose_name il campo si chiamerebbe "Quantita" (senza accento)
    quantita = models.PositiveIntegerField(
        default=1,
        verbose_name="Quantità"
    )

    # verbose_name "Data ordine" → chiarisce il significato del campo
    # auto_now_add=True significa che la data viene impostata automaticamente
    # al momento della creazione e non può essere modificata
    data = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data ordine"
    )

    class Meta:
        # verbose_name → "L'Ordine è stato salvato con successo"
        verbose_name = "Ordine"

        # verbose_name_plural → voce nel menu dell'admin
        # senza questo Django scriverebbe "Ordines"
        verbose_name_plural = "Ordini"

        # ordering → gli ordini più recenti appaiono per primi
        # il - davanti a data significa ORDER BY data DESC
        ordering = ['-data']

    def __str__(self):
        return f"Ordine #{self.id} — {self.prodotto.nome}"
```

---

## Riepilogo finale

| | `verbose_name` nel campo | `verbose_name` nella Meta |
|---|---|---|
| **Dove appare** | Etichetta del campo nel form | Nome del modello nel menu admin |
| **Cosa controlla** | Il singolo campo | Il modello intero |
| **Forma** | Stringa singola | Singolare + plurale |
| **Obbligatorio** | No | No, ma `_plural` è quasi sempre necessario |
| **Esempio** | `"Prezzo (€)"` | `"Prodotto"` / `"Prodotti"` |
