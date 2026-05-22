# Esercizio 2 — Filtraggio, Ordinamento e Aggregazioni con Django ORM

Questa guida copre tutto, dall'installazione dell'ambiente virtuale Python fino all'esecuzione delle query Django ORM, spiegando ogni concetto nel dettaglio.

---

## Indice

1. [Creare l'ambiente virtuale Python](#1-creare-lambiente-virtuale-python)
2. [Installare Django](#2-installare-django)
3. [Creare il progetto e l'app](#3-creare-il-progetto-e-lapp)
4. [Configurare settings.py](#4-configurare-settingspy)
5. [I Modelli — models.py](#5-i-modelli--modelspy)
6. [La classe Meta — cos'è e dove va](#6-la-classe-meta--cosè-e-dove-va)
7. [Registrare i modelli nell'admin](#7-registrare-i-modelli-nelladmin)
8. [Migrazioni e avvio del server](#8-migrazioni-e-avvio-del-server)
9. [Creare il superuser](#9-creare-il-superuser)
10. [Inserire dati di test](#10-inserire-dati-di-test)
11. [Le consegne — Query ORM](#11-le-consegne--query-orm)

---

## 1. Creare l'ambiente virtuale Python

L'ambiente virtuale isola le dipendenze del progetto dal resto del sistema. In questo modo ogni progetto ha le sue librerie senza conflitti.

```bash
python -m venv venv
```

Questo crea una cartella `venv/` nella directory del progetto.

### Attivare l'ambiente virtuale

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

Quando l'ambiente è attivo vedrai `(venv)` all'inizio del terminale:

```
(venv) PS D:\negozio_django>
```

> Devi attivare l'ambiente virtuale ogni volta che apri un nuovo terminale prima di lavorare sul progetto.

---

## 2. Installare Django

Con l'ambiente virtuale attivo:

```bash
pip install django
```

Per verificare che sia stato installato correttamente:

```bash
python -m django --version
```

---

## 3. Creare il progetto e l'app

### Creare il progetto

```bash
django-admin startproject config .
```

Il `.` alla fine dice a Django di creare i file nella cartella corrente invece di creare una sottocartella aggiuntiva.

> **Perché `config` e non il nome del progetto?**
> **Senza il `.`** — Django crea una cartella del progetto e dentro mette la configurazione con lo stesso nome:
> ```
> negozio_django/          ← creata da Django
>   ├── negozio_django/    ← configurazione (stesso nome!)
>   │   ├── settings.py
>   │   └── urls.py
>   └── manage.py
> ```
>
> **Con il `.`** — Django usa la cartella in cui sei già, ma la configurazione ha ancora lo stesso nome:
> ```
> negozio_django/          ← cartella in cui sei già
>   ├── negozio_django/    ← configurazione (stesso nome!)
>   │   ├── settings.py
>   │   └── urls.py
>   └── manage.py
> ```
>
> **Usando `config .`** — usi la cartella in cui sei già e la configurazione ha un nome diverso e riconoscibile:
> ```
> negozio_django/          ← cartella in cui sei già
>   ├── config/            ← chiaramente la configurazione
>   │   ├── settings.py
>   │   └── urls.py
>   └── manage.py
> ```
### Creare l'app

```bash
python manage.py startapp negozio
```

### Struttura risultante

```
negozio_django/
  ├── config/               ← configurazione del progetto
  │   ├── settings.py       ← impostazioni generali
  │   ├── urls.py           ← routing URL principale
  │   └── wsgi.py
  ├── negozio/              ← la tua app
  │   ├── models.py         ← definizione dei modelli (tabelle DB)
  │   ├── views.py          ← logica delle pagine
  │   ├── admin.py          ← pannello di amministrazione
  │   └── migrations/       ← storico delle modifiche al DB
  ├── venv/
  ├── db.sqlite3            ← il database (creato dopo migrate)
  └── manage.py             ← strumento da riga di comando Django
```

> **Differenza tra progetto e app:** il progetto (`config`) è il contenitore generale con le impostazioni. L'app (`negozio`) è un modulo funzionale con i suoi modelli, viste e URL.

---

## 4. Configurare settings.py

Apri `config/settings.py` e aggiungi il nome della tua app in `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'negozio',    # ← aggiungi il nome della tua app
]
```

Senza questa riga Django non sa che la tua app esiste e le migrazioni non funzioneranno.

---

## 5. I Modelli — models.py

I modelli definiscono la struttura del database. Ogni classe corrisponde a una tabella, ogni attributo a una colonna.

Apri `negozio/models.py` e scrivi:

```python
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome categoria"   # ← nome del campo nell'admin
    )

    class Meta:
        verbose_name        = "Categoria"
        verbose_name_plural = "Categorie"
        ordering            = ['nome']

    def __str__(self):
        return self.nome


class Prodotto(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome prodotto"
    )
    prezzo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prezzo (€)"
    )
    in_stock = models.BooleanField(
        default=True,
        verbose_name="Disponibile"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='prodotti',
        verbose_name="Categoria"
    )

    class Meta:
        verbose_name        = "Prodotto"
        verbose_name_plural = "Prodotti"
        ordering            = ['prezzo']

    def __str__(self):
        return f"{self.nome} — {self.prezzo}€"


class Ordine(models.Model):
    prodotto = models.ForeignKey(
        Prodotto,
        on_delete=models.CASCADE,
        related_name='ordini',
        verbose_name="Prodotto"
    )
    quantita = models.PositiveIntegerField(
        default=1,
        verbose_name="Quantità"
    )
    data = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data ordine"
    )

    class Meta:
        verbose_name        = "Ordine"
        verbose_name_plural = "Ordini"
        ordering            = ['-data']   # ordini più recenti prima

    def __str__(self):
        return f"Ordine #{self.id} — {self.prodotto.nome}"
```

### Tipi di campo usati

| Campo | Uso |
|---|---|
| `CharField` | Testo breve (nome, titolo) |
| `DecimalField` | Numeri decimali precisi (prezzi, valute) |
| `BooleanField` | Vero/Falso |
| `ForeignKey` | Relazione molti-a-uno con un altro modello |
| `PositiveIntegerField` | Numero intero positivo |
| `DateTimeField` | Data e ora |

> **Perché `DecimalField` e non `FloatField` per i prezzi?**
> I `float` in Python hanno problemi di precisione (es. `0.1 + 0.2 = 0.30000000000000004`).
> `DecimalField` garantisce precisione esatta, fondamentale per i valori monetari.

### Relazioni tra i modelli

```
Categoria
    │
    │ 1 ──── N
    │
Prodotto ──── 1 ──── N ──── Ordine
```

Una `Categoria` può avere molti `Prodotto`. Un `Prodotto` può avere molti `Ordine`.

---

## 6. La classe Meta — cos'è e dove va

La classe `Meta` è una classe **interna** che si scrive dentro un modello Django. Non crea nessuna colonna nel database — serve solo a configurare il **comportamento del modello nel suo complesso**.

### Dove va

Sempre dentro il modello, dopo i campi e prima di `__str__`:

```python
class Prodotto(models.Model):
    # 1. Prima i campi
    nome   = models.CharField(max_length=200)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)

    # 2. Poi la classe Meta
    class Meta:
        verbose_name        = "Prodotto"
        verbose_name_plural = "Prodotti"
        ordering            = ['prezzo']

    # 3. Infine __str__
    def __str__(self):
        return self.nome
```

### Differenza tra verbose_name nel campo e nella Meta

Sono due cose diverse che appaiono in posti diversi nell'admin:

**`verbose_name` nel campo** → è il nome della singola etichetta nel form:

```python
prezzo = models.DecimalField(verbose_name="Prezzo (€)")
```

Lo vedi nel form quando apri un prodotto:
```
Nome prodotto   [_____________]
Prezzo (€)      [_____________]   ← verbose_name del campo
Disponibile     [ ]
```

**`verbose_name` nella Meta** → è il nome del modello nel menu dell'admin:

```python
class Meta:
    verbose_name        = "Prodotto"    # singolare
    verbose_name_plural = "Prodotti"    # plurale nel menu
```

Lo vedi nella navigazione:
```
NEGOZIO
  ├── Categorie    ← verbose_name_plural di Categoria
  ├── Prodotti     ← verbose_name_plural di Prodotto
  └── Ordini       ← verbose_name_plural di Ordine
```

> **Senza `verbose_name_plural`** Django aggiunge automaticamente una "s" in inglese al nome della classe: `Ordine` diventerebbe `Ordines` nel pannello admin.

### Le opzioni più comuni di Meta

```python
class Meta:
    # Nome leggibile nell'admin (singolare e plurale)
    verbose_name        = "Prodotto"
    verbose_name_plural = "Prodotti"

    # Ordinamento di default dei risultati
    ordering = ['prezzo']      # crescente
    ordering = ['-prezzo']     # decrescente (il - inverte)
    ordering = ['-data', 'nome']  # prima per data desc, poi nome asc

    # Nome della tabella nel database (default: nomeapp_nomemodello)
    db_table = "shop_prodotti"
```

---

## 7. Registrare i modelli nell'admin

Apri `negozio/admin.py`:

```python
from django.contrib import admin
from .models import Categoria, Prodotto, Ordine

admin.site.register(Categoria)
admin.site.register(Prodotto)
admin.site.register(Ordine)
```

Senza questo passaggio i modelli non appaiono nel pannello admin anche se sono stati creati correttamente.

---

## 8. Migrazioni e avvio del server

Le migrazioni traducono i tuoi modelli Python in tabelle SQL nel database.

```bash
# Crea i file di migrazione (analizza models.py)
python manage.py makemigrations

# Applica le migrazioni al database
python manage.py migrate

# Avvia il server di sviluppo
python manage.py runserver
```

Vai su `http://127.0.0.1:8000` per vedere Django in funzione.

> **Regola da ricordare:** ogni volta che modifichi `models.py` devi rieseguire `makemigrations` e `migrate`.

---

## 9. Creare il superuser

Il superuser serve per accedere al pannello admin. Devi fare `migrate` **prima** di crearlo, altrimenti Django non trova la tabella degli utenti nel database.

```bash
python manage.py createsuperuser
```

Inserisci le credenziali richieste:

```
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********

Superuser created successfully.
```

Accedi all'admin su `http://127.0.0.1:8000/admin`.

---

## 10. Inserire dati di test

Apri la shell interattiva di Django:

```bash
python manage.py shell
```

Incolla questi comandi per popolare il database:

```python
from negozio.models import Categoria, Prodotto, Ordine

# Categorie
elettronica   = Categoria.objects.create(nome="Elettronica")
abbigliamento = Categoria.objects.create(nome="Abbigliamento")

# Prodotti
p1 = Prodotto.objects.create(nome="Smartphone", prezzo=499, in_stock=True,  categoria=elettronica)
p2 = Prodotto.objects.create(nome="Laptop",     prezzo=999, in_stock=True,  categoria=elettronica)
p3 = Prodotto.objects.create(nome="Cuffie",     prezzo=79,  in_stock=True,  categoria=elettronica)
p4 = Prodotto.objects.create(nome="TV 4K",      prezzo=799, in_stock=False, categoria=elettronica)
p5 = Prodotto.objects.create(nome="T-shirt",    prezzo=25,  in_stock=True,  categoria=abbigliamento)
p6 = Prodotto.objects.create(nome="Jeans",      prezzo=59,  in_stock=True,  categoria=abbigliamento)
p7 = Prodotto.objects.create(nome="Tablet",     prezzo=349, in_stock=True,  categoria=elettronica)
p8 = Prodotto.objects.create(nome="Smartwatch", prezzo=199, in_stock=True,  categoria=elettronica)

# Ordini
Ordine.objects.create(prodotto=p3, quantita=2)
Ordine.objects.create(prodotto=p3, quantita=1)
Ordine.objects.create(prodotto=p1, quantita=1)

print("Dati inseriti con successo!")
```

---

## 11. Le consegne — Query ORM

Apri la shell con `python manage.py shell` per eseguire le query.

---

### Consegna 01 — Prodotti tra 10€ e 100€, ordinati per prezzo crescente

**Senza list comprehension:**

```python
from negozio.models import Prodotto

risultato = Prodotto.objects.filter(prezzo__range=(10, 100)).order_by('prezzo')

for p in risultato:
    print(p.nome, p.prezzo)
```

**Con list comprehension:**

```python
from negozio.models import Prodotto

risultato = Prodotto.objects.filter(prezzo__range=(10, 100)).order_by('prezzo')

[print(p.nome, p.prezzo) for p in risultato]
```

**Spiegazione:**
- `filter(prezzo__range=(10, 100))` usa il lookup `__range` che equivale a `WHERE prezzo BETWEEN 10 AND 100` in SQL
- `.order_by('prezzo')` ordina in modo crescente (ASC). Per decrescente si usa `'-prezzo'`

**Risultato atteso:**
```
T-shirt  25.00
Jeans    59.00
Cuffie   79.00
```

---

### Consegna 02 — Elettronica, in stock, prezzo ≤ 500€

**Senza list comprehension:**

```python
risultato = Prodotto.objects.filter(
    categoria__nome='Elettronica',
    in_stock=True
).exclude(prezzo__gt=500)

for p in risultato:
    print(p.nome, p.prezzo)
```

**Con list comprehension:**

```python
risultato = Prodotto.objects.filter(
    categoria__nome='Elettronica',
    in_stock=True
).exclude(prezzo__gt=500)

[print(p.nome, p.prezzo) for p in risultato]
```

**Spiegazione:**
- `categoria__nome='Elettronica'` usa il doppio underscore `__` per navigare la ForeignKey e filtrare per il nome della categoria collegata
- `in_stock=True` filtra solo i prodotti disponibili
- `.exclude(prezzo__gt=500)` esclude i prodotti con prezzo maggiore di 500€. Equivalente a scrivere `filter(prezzo__lte=500)`

**Risultato atteso:**
```
Cuffie      79.00
Smartwatch  199.00
Tablet      349.00
Smartphone  499.00
```

---

### Consegna 03 — Conta gli ordini per il prodotto con id=3

**Senza list comprehension:**

```python
from negozio.models import Ordine

numero = Ordine.objects.filter(prodotto__id=3).count()
print(f"Ordini per prodotto id=3: {numero}")
```

**Con list comprehension** (non applicabile qui, `.count()` restituisce già un intero):

```python
from negozio.models import Ordine

numero = Ordine.objects.filter(prodotto__id=3).count()
print(f"Ordini per prodotto id=3: {numero}")
```

**Spiegazione:**
- `filter(prodotto__id=3)` filtra gli ordini che hanno come prodotto collegato quello con id=3
- `.count()` restituisce direttamente un intero con `SELECT COUNT(*)` — è più efficiente di `len(queryset)`

**Risultato atteso:**
```
Ordini per prodotto id=3: 2
```

---

### Consegna 04 — Prezzo medio, minimo e massimo dei prodotti in stock

**Senza list comprehension:**

```python
from django.db.models import Avg, Min, Max

risultato = Prodotto.objects.filter(in_stock=True).aggregate(
    media=Avg('prezzo'),
    minimo=Min('prezzo'),
    massimo=Max('prezzo')
)
print(risultato)
```

**Con list comprehension** (per stampare in modo leggibile):

```python
from django.db.models import Avg, Min, Max

risultato = Prodotto.objects.filter(in_stock=True).aggregate(
    media=Avg('prezzo'),
    minimo=Min('prezzo'),
    massimo=Max('prezzo')
)

[print(f"{k}: {v}") for k, v in risultato.items()]
```

**Spiegazione:**
- `.aggregate()` esegue calcoli sull'intero queryset e restituisce un **dizionario**, non un queryset
- `Avg`, `Min`, `Max` vengono importate da `django.db.models`
- Si possono combinare più aggregazioni in una sola query SQL
- Il TV 4K è escluso perché ha `in_stock=False`

**Risultato atteso:**
```
{'media': Decimal('315.57'), 'minimo': Decimal('25'), 'massimo': Decimal('999')}
```

---

### Consegna 05 — I 5 prodotti più costosi (solo nome e prezzo)

**Senza list comprehension:**

```python
risultato = Prodotto.objects.order_by('-prezzo').values('nome', 'prezzo')[:5]

for p in risultato:
    print(p['nome'], p['prezzo'])
```

**Con list comprehension:**

```python
risultato = Prodotto.objects.order_by('-prezzo').values('nome', 'prezzo')[:5]

[print(p['nome'], p['prezzo']) for p in risultato]
```

**Spiegazione:**
- `.order_by('-prezzo')` ordina in modo **decrescente** grazie al `-` davanti al nome del campo
- `.values('nome', 'prezzo')` proietta solo i campi richiesti, come `SELECT nome, prezzo` in SQL. Restituisce dizionari invece di oggetti modello, quindi si accede ai campi con `p['nome']` invece di `p.nome`
- `[:5]` è uno slice del queryset che equivale a `LIMIT 5` in SQL

**Risultato atteso:**
```
Laptop      999.00
TV 4K       799.00
Smartphone  499.00
Tablet      349.00
Smartwatch  199.00
```

---

## Riepilogo dei Field Lookups usati

| Lookup | Significato | Esempio |
|---|---|---|
| `__range` | BETWEEN x AND y | `prezzo__range=(10, 100)` |
| `__gte` | >= (greater than or equal) | `prezzo__gte=10` |
| `__lte` | <= (less than or equal) | `prezzo__lte=100` |
| `__gt` | > (greater than) | `prezzo__gt=500` |
| `__lt` | < (less than) | `prezzo__lt=500` |
| `__` | naviga ForeignKey | `categoria__nome='Elettronica'` |

---

## Riepilogo ordine operazioni dall'inizio

| Step | Comando |
|---|---|
| 1 | `python -m venv venv` |
| 2 | `venv\Scripts\activate` (Windows) |
| 3 | `pip install django` |
| 4 | `django-admin startproject config .` |
| 5 | `python manage.py startapp negozio` |
| 6 | Aggiungi `'negozio'` in `INSTALLED_APPS` |
| 7 | Scrivi i modelli in `models.py` |
| 8 | Registra i modelli in `admin.py` |
| 9 | `python manage.py makemigrations` |
| 10 | `python manage.py migrate` |
| 11 | `python manage.py createsuperuser` |
| 12 | `python manage.py runserver` |
