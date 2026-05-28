# Libreria Musicale — Django Project

## Indice
1. [Inizializzazione del progetto](#1-inizializzazione-del-progetto)
2. [Struttura del progetto](#2-struttura-del-progetto)
3. [Definizione dei Model](#3-definizione-dei-model)
4. [Migrazioni](#4-migrazioni)
5. [Superuser e pannello Admin](#5-superuser-e-pannello-admin)
6. [Popolamento del database](#6-popolamento-del-database)
7. [QuerySet — Esercizi](#7-queryset--esercizi)
8. [Tabella dei metodi ORM](#8-tabella-dei-metodi-orm)

---

## 1. Inizializzazione del progetto

### Creare il progetto Django
```bash
django-admin startproject config .
```
Il `.` finale è importante: dice a Django di creare i file del progetto **nella cartella corrente** invece di creare una sottocartella. `config` è il nome della cartella di configurazione (contiene `settings.py`, `urls.py`, `wsgi.py`). Senza il `.` Django creerebbe una cartella `config/config/` annidata.

### Creare l'app
```bash
python manage.py startapp catalogo
```
Un progetto Django è diviso in **app** — moduli riutilizzabili con le proprie logiche. `catalogo` è l'app che gestisce artisti, album e canzoni.

### Registrare l'app in settings.py
```python
# musiclib/settings.py
INSTALLED_APPS = [
    ...
    'catalogo',  # aggiungere questa riga
]
```
Django deve sapere che l'app esiste per poterne gestire i model e le migrazioni.

---

## 2. Struttura del progetto

```
musiclib/
├── config/
│   ├── settings.py      # configurazione globale
│   ├── urls.py          # routing URL principale
│   └── wsgi.py
├── catalogo/
│   ├── models.py        # definizione dei Model ← lavoriamo qui
│   ├── admin.py         # registrazione nell'admin
│   ├── views.py
│   └── migrations/      # cartella auto-generata dalle migrazioni
└── manage.py            # comando principale Django
```

---

## 3. Definizione dei Model

I **Model** sono classi Python che rappresentano le tabelle del database. Ogni attributo della classe corrisponde a una colonna.

```python
# catalogo/models.py

from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=150)
    # CharField: testo breve con limite di caratteri (validato anche nel DB)
    
    nazionalita = models.CharField(max_length=100, blank=True)
    # blank=True: il campo è opzionale nei form (può essere lasciato vuoto)
    
    biografia = models.TextField(blank=True)
    # TextField: testo lungo senza limite di caratteri nel DB
    
    data_debutto = models.DateField(null=True, blank=True)
    # null=True: il DB può salvare NULL (necessario per date e numeri)
    # blank=True: il form può ricevere un valore vuoto

    def __str__(self):
        return f"{self.nome} ({self.nazionalita}) - Album: {self.albums.count()}"
    # __str__: rappresentazione leggibile dell'oggetto (usata nell'admin e nella shell)

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artisti"
        ordering = ['nome']
        # ordering: ordine di default nelle query (alfabetico per nome)


class Album(models.Model):
    titolo = models.CharField(max_length=200)
    
    artista = models.ForeignKey(
        Artista,
        on_delete=models.PROTECT,
        related_name='albums'
    )
    # ForeignKey: relazione molti-a-uno (molti album → un artista)
    # on_delete=PROTECT: impedisce la cancellazione dell'Artista se ha Album collegati
    # related_name='albums': permette di accedere agli album da un artista con artista.albums.all()
    
    anno = models.IntegerField()
    
    GENERE_CHOICES = [
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Jazz', 'Jazz'),
        ('Classica', 'Classica'),
        ('Altro', 'Altro'),
    ]
    genere = models.CharField(
        max_length=10,
        choices=GENERE_CHOICES,
        default='Altro'
    )
    # choices: limita i valori accettati (dropdown nell'admin)
    
    disponibile = models.BooleanField(default=True)
    # BooleanField: valore True/False, default=True significa disponibile per default

    def __str__(self):
        return f"{self.titolo} - {self.artista.nome} - {self.anno} - {self.genere}"

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Album"
        ordering = ['anno']


class Canzone(models.Model):
    titolo = models.CharField(max_length=200)
    
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='canzoni'
    )
    # on_delete=CASCADE: se si cancella un Album, tutte le sue Canzoni vengono cancellate automaticamente
    
    durata_secondi = models.IntegerField(verbose_name="Durata in secondi")
    # verbose_name: etichetta leggibile mostrata nell'admin
    
    traccia = models.IntegerField(verbose_name="Numero di traccia")

    def __str__(self):
        return f"{self.titolo} - {self.album.titolo} - {self.durata_secondi} secondi - traccia {self.traccia}"

    class Meta:
        verbose_name = "Canzone"
        verbose_name_plural = "Canzoni"
        ordering = ['traccia']
```

### Differenza tra `null=True` e `blank=True`

| | `null=True` | `blank=True` |
|---|---|---|
| Agisce su | Database | Form / validazione |
| Cosa permette | Salvare NULL nel DB | Lasciare vuoto il campo nel form |
| Quando usarlo | Date, numeri, FK opzionali | Tutti i campi opzionali |
| Testo (`CharField`, `TextField`) | Non necessario (usa stringa vuota `""`) | Sì, per campi opzionali |

### Differenza tra `on_delete=PROTECT` e `CASCADE`

| | `PROTECT` | `CASCADE` |
|---|---|---|
| Cosa fa | Blocca la cancellazione del padre se ha figli | Cancella i figli automaticamente con il padre |
| Usato su | `Album → Artista` (protegge l'artista) | `Canzone → Album` (cancella le canzoni con l'album) |
| Errore se si tenta di cancellare il padre con figli | Sì — `ProtectedError` | No — i figli vengono eliminati |

---

## 4. Migrazioni

Le **migrazioni** sono file che traducono le modifiche ai Model in istruzioni SQL per il database.

```bash
# Genera i file di migrazione analizzando i Model
python manage.py makemigrations

# Applica le migrazioni al database
python manage.py migrate
```

> Ogni volta che si modifica un Model (aggiunta di campi, modifica di tipo, ecc.) bisogna rieseguire entrambi i comandi.

---

## 5. Superuser e pannello Admin

### Creare il superuser
```bash
python manage.py createsuperuser
```
```
Username: Rosa
Password: 1234
```

### Registrare i Model nell'admin

```python
# catalogo/admin.py
from django.contrib import admin
from .models import Artista, Album, Canzone


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nazionalita', 'data_debutto')
    # list_display: colonne visibili nella lista dell'admin
    search_fields = ('nome', 'nazionalita')
    # search_fields: campi su cui funziona la barra di ricerca
    ordering = ('nome',)
    # ordering: ordinamento di default nella lista


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'artista', 'anno', 'genere')
    list_filter = ('genere', 'anno')
    # list_filter: filtri laterali nella lista
    search_fields = ('titolo', 'artista__nome')
    # artista__nome: traversata FK per cercare anche per nome artista
    ordering = ('anno',)


@admin.register(Canzone)
class CanzoneAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'album', 'traccia', 'durata_secondi')
    list_filter = ('album',)
    search_fields = ('titolo', 'album__titolo')
    ordering = ('traccia',)
```

`@admin.register(Model)` è il modo moderno di registrare un model — equivale a `admin.site.register(Canzone, CanzoneAdmin)` ma più leggibile.

### Avviare il server
```bash
python manage.py runserver
```
Pannello admin disponibile su: `http://127.0.0.1:8000/admin/`

---

## 6. Popolamento del database

### Aprire la shell Django
```bash
python manage.py shell
```
La shell è un interprete Python interattivo con il contesto Django già configurato — permette di usare i Model direttamente.

### Script di popolamento — Artisti Rock/Pop

```python
from catalogo.models import Artista, Album, Canzone
from datetime import date

beatles = Artista.objects.create(nome="The Beatles", nazionalita="Britannica", data_debutto=date(1960, 8, 1))
floyd = Artista.objects.create(nome="Pink Floyd", nazionalita="Britannica", data_debutto=date(1965, 1, 1))
bowie = Artista.objects.create(nome="David Bowie", nazionalita="Britannica", data_debutto=date(1964, 1, 1))
zeppelin = Artista.objects.create(nome="Led Zeppelin", nazionalita="Britannica", data_debutto=date(1968, 1, 1))
queen = Artista.objects.create(nome="Queen", nazionalita="Britannica", data_debutto=date(1970, 1, 1))
jackson = Artista.objects.create(nome="Michael Jackson", nazionalita="Americana", data_debutto=date(1964, 1, 1))
radiohead = Artista.objects.create(nome="Radiohead", nazionalita="Britannica", data_debutto=date(1985, 1, 1))
nirvana = Artista.objects.create(nome="Nirvana", nazionalita="Americana", data_debutto=date(1987, 1, 1))
daftpunk = Artista.objects.create(nome="Daft Punk", nazionalita="Francese", data_debutto=date(1993, 1, 1))
depeche = Artista.objects.create(nome="Depeche Mode", nazionalita="Britannica", data_debutto=date(1980, 1, 1))
abbey = Album.objects.create(titolo="Abbey Road", artista=beatles, anno=1969, genere="Rock")
Canzone.objects.create(titolo="Come Together", album=abbey, durata_secondi=259, traccia=1)
Canzone.objects.create(titolo="Something", album=abbey, durata_secondi=182, traccia=2)
Canzone.objects.create(titolo="Here Comes the Sun", album=abbey, durata_secondi=185, traccia=3)
pepper = Album.objects.create(titolo="Sgt. Pepper's", artista=beatles, anno=1967, genere="Rock")
Canzone.objects.create(titolo="Lucy in the Sky", album=pepper, durata_secondi=208, traccia=1)
Canzone.objects.create(titolo="With a Little Help", album=pepper, durata_secondi=163, traccia=2)
wall = Album.objects.create(titolo="The Wall", artista=floyd, anno=1979, genere="Rock")
Canzone.objects.create(titolo="Another Brick Pt.2", album=wall, durata_secondi=238, traccia=1)
Canzone.objects.create(titolo="Comfortably Numb", album=wall, durata_secondi=382, traccia=2)
Canzone.objects.create(titolo="Hey You", album=wall, durata_secondi=284, traccia=3)
dark = Album.objects.create(titolo="The Dark Side of the Moon", artista=floyd, anno=1973, genere="Rock")
Canzone.objects.create(titolo="Money", album=dark, durata_secondi=382, traccia=1)
Canzone.objects.create(titolo="Time", album=dark, durata_secondi=421, traccia=2)
ziggy = Album.objects.create(titolo="Ziggy Stardust", artista=bowie, anno=1972, genere="Rock")
Canzone.objects.create(titolo="Starman", album=ziggy, durata_secondi=255, traccia=1)
Canzone.objects.create(titolo="Suffragette City", album=ziggy, durata_secondi=213, traccia=2)
heroes = Album.objects.create(titolo="Heroes", artista=bowie, anno=1977, genere="Rock")
Canzone.objects.create(titolo="Heroes", album=heroes, durata_secondi=360, traccia=1)
Canzone.objects.create(titolo="Beauty and the Beast", album=heroes, durata_secondi=220, traccia=2)
lz4 = Album.objects.create(titolo="Led Zeppelin IV", artista=zeppelin, anno=1971, genere="Rock")
Canzone.objects.create(titolo="Stairway to Heaven", album=lz4, durata_secondi=482, traccia=1)
Canzone.objects.create(titolo="Black Dog", album=lz4, durata_secondi=294, traccia=2)
Canzone.objects.create(titolo="Rock and Roll", album=lz4, durata_secondi=220, traccia=3)
night = Album.objects.create(titolo="A Night at the Opera", artista=queen, anno=1975, genere="Rock")
Canzone.objects.create(titolo="Bohemian Rhapsody", album=night, durata_secondi=354, traccia=1)
Canzone.objects.create(titolo="You're My Best Friend", album=night, durata_secondi=170, traccia=2)
jazz = Album.objects.create(titolo="Jazz", artista=queen, anno=1978, genere="Rock")
Canzone.objects.create(titolo="Don't Stop Me Now", album=jazz, durata_secondi=209, traccia=1)
Canzone.objects.create(titolo="Fat Bottomed Girls", album=jazz, durata_secondi=252, traccia=2)
thriller = Album.objects.create(titolo="Thriller", artista=jackson, anno=1982, genere="Pop")
Canzone.objects.create(titolo="Thriller", album=thriller, durata_secondi=358, traccia=1)
Canzone.objects.create(titolo="Billie Jean", album=thriller, durata_secondi=294, traccia=2)
Canzone.objects.create(titolo="Beat It", album=thriller, durata_secondi=258, traccia=3)
bad = Album.objects.create(titolo="Bad", artista=jackson, anno=1987, genere="Pop")
Canzone.objects.create(titolo="Bad", album=bad, durata_secondi=247, traccia=1)
Canzone.objects.create(titolo="Man in the Mirror", album=bad, durata_secondi=319, traccia=2)
ok = Album.objects.create(titolo="OK Computer", artista=radiohead, anno=1997, genere="Rock")
Canzone.objects.create(titolo="Paranoid Android", album=ok, durata_secondi=383, traccia=1)
Canzone.objects.create(titolo="Karma Police", album=ok, durata_secondi=263, traccia=2)
Canzone.objects.create(titolo="No Surprises", album=ok, durata_secondi=228, traccia=3)
nev = Album.objects.create(titolo="Nevermind", artista=nirvana, anno=1991, genere="Rock")
Canzone.objects.create(titolo="Smells Like Teen Spirit", album=nev, durata_secondi=301, traccia=1)
Canzone.objects.create(titolo="Come as You Are", album=nev, durata_secondi=219, traccia=2)
Canzone.objects.create(titolo="Lithium", album=nev, durata_secondi=256, traccia=3)
discovery = Album.objects.create(titolo="Discovery", artista=daftpunk, anno=2001, genere="Pop")
Canzone.objects.create(titolo="One More Time", album=discovery, durata_secondi=320, traccia=1)
Canzone.objects.create(titolo="Digital Love", album=discovery, durata_secondi=301, traccia=2)
Canzone.objects.create(titolo="Harder Better Faster", album=discovery, durata_secondi=224, traccia=3)
ram = Album.objects.create(titolo="Random Access Memories", artista=daftpunk, anno=2013, genere="Pop")
Canzone.objects.create(titolo="Get Lucky", album=ram, durata_secondi=369, traccia=1)
Canzone.objects.create(titolo="Instant Crush", album=ram, durata_secondi=337, traccia=2)
viol = Album.objects.create(titolo="Violator", artista=depeche, anno=1990, genere="Pop")
Canzone.objects.create(titolo="Personal Jesus", album=viol, durata_secondi=228, traccia=1)
Canzone.objects.create(titolo="Enjoy the Silence", album=viol, durata_secondi=276, traccia=2)
Canzone.objects.create(titolo="Policy of Truth", album=viol, durata_secondi=245, traccia=3)
print(f"Artisti: {Artista.objects.count()}, Album: {Album.objects.count()}, Canzoni: {Canzone.objects.count()}")
```

### Script di popolamento — Artisti Jazz (aggiunto dopo)

```python
from catalogo.models import Artista, Album, Canzone
from datetime import date

coltrane = Artista.objects.create(nome="John Coltrane", nazionalita="Americana", data_debutto=date(1955, 1, 1))
davis = Artista.objects.create(nome="Miles Davis", nazionalita="Americana", data_debutto=date(1944, 1, 1))
kind = Album.objects.create(titolo="Kind of Blue", artista=davis, anno=1959, genere="Jazz")
Canzone.objects.create(titolo="So What", album=kind, durata_secondi=562, traccia=1)
Canzone.objects.create(titolo="Freddie Freeloader", album=kind, durata_secondi=589, traccia=2)
Canzone.objects.create(titolo="Blue in Green", album=kind, durata_secondi=337, traccia=3)
love = Album.objects.create(titolo="A Love Supreme", artista=coltrane, anno=1965, genere="Jazz")
Canzone.objects.create(titolo="Acknowledgement", album=love, durata_secondi=473, traccia=1)
Canzone.objects.create(titolo="Resolution", album=love, durata_secondi=438, traccia=2)
Canzone.objects.create(titolo="Pursuance", album=love, durata_secondi=667, traccia=3)
print(f"Artisti: {Artista.objects.count()}, Album: {Album.objects.count()}, Canzoni: {Canzone.objects.count()}")
```

### Comandi di verifica nella shell

```python
# Verifica artisti Jazz inseriti
Artista.objects.filter(nome__in=["John Coltrane", "Miles Davis"])

# Verifica album Jazz
Album.objects.filter(genere="Jazz")

# Verifica canzoni Jazz tramite traversata FK
Canzone.objects.filter(album__genere="Jazz")

# Verifica quale album corrisponde a un certo pk
Album.objects.get(pk=5)

# Verifica le canzoni di quell'album
Album.objects.get(pk=5).canzoni.all()
```

---

## 7. QuerySet — Esercizi

Aprire la shell con `python manage.py shell` e importare i model:

```python
from catalogo.models import Artista, Album, Canzone
```

### Query 1 — Tutti gli album dal più recente al più antico

```python
Album.objects.all().order_by('-anno')
```

Il `-` davanti al campo inverte l'ordinamento (decrescente). Senza `-` sarebbe crescente.

Output atteso:
```
<QuerySet [
  <Album: Random Access Memories - Daft Punk - 2013 - Pop>,
  <Album: Discovery - Daft Punk - 2001 - Pop>,
  <Album: OK Computer - Radiohead - 1997 - Rock>,
  <Album: Nevermind - Nirvana - 1991 - Rock>,
  <Album: Violator - Depeche Mode - 1990 - Pop>,
  <Album: Bad - Michael Jackson - 1987 - Pop>,
  <Album: Thriller - Michael Jackson - 1982 - Pop>,
  <Album: The Wall - Pink Floyd - 1979 - Rock>,
  <Album: Jazz - Queen - 1978 - Rock>,
  <Album: Heroes - David Bowie - 1977 - Rock>,
  <Album: A Night at the Opera - Queen - 1975 - Rock>,
  <Album: The Dark Side of the Moon - Pink Floyd - 1973 - Rock>,
  <Album: Ziggy Stardust - David Bowie - 1972 - Rock>,
  <Album: Led Zeppelin IV - Led Zeppelin - 1971 - Rock>,
  <Album: Abbey Road - The Beatles - 1969 - Rock>,
  <Album: Sgt. Pepper's - The Beatles - 1967 - Rock>,
  <Album: A Love Supreme - John Coltrane - 1965 - Jazz>,
  <Album: Kind of Blue - Miles Davis - 1959 - Jazz>
]>
```

### Query 2 — Album Rock oppure Jazz (condizione OR)

```python
from django.db.models import Q
Album.objects.filter(Q(genere='Rock') | Q(genere='Jazz'))
```

`Q()` è necessario per le condizioni OR. I `.filter()` concatenati fanno sempre AND. Il `|` è l'operatore OR tra due oggetti `Q`.

Output atteso:
```
<QuerySet [
  <Album: Kind of Blue - Miles Davis - 1959 - Jazz>,
  <Album: A Love Supreme - John Coltrane - 1965 - Jazz>,
  <Album: Sgt. Pepper's - The Beatles - 1967 - Rock>,
  <Album: Abbey Road - The Beatles - 1969 - Rock>,
  <Album: Led Zeppelin IV - Led Zeppelin - 1971 - Rock>,
  <Album: Ziggy Stardust - David Bowie - 1972 - Rock>,
  <Album: The Dark Side of the Moon - Pink Floyd - 1973 - Rock>,
  <Album: A Night at the Opera - Queen - 1975 - Rock>,
  <Album: Heroes - David Bowie - 1977 - Rock>,
  <Album: Jazz - Queen - 1978 - Rock>,
  <Album: The Wall - Pink Floyd - 1979 - Rock>,
  <Album: Nevermind - Nirvana - 1991 - Rock>,
  <Album: OK Computer - Radiohead - 1997 - Rock>
]>
```

### Query 3 — Quante canzoni ha l'album con pk=5

```python
Canzone.objects.filter(album__pk=5).count()
```

`album__pk` è una traversata FK: parte da `Canzone`, attraversa la FK `album`, arriva al campo `pk`. `.count()` restituisce un intero, non un QuerySet.

Output atteso: `2`

> Nota: `pk=5` corrisponde a `Ziggy Stardust` di David Bowie, che ha 2 canzoni (Starman e Suffragette City). Il pk dipende dall'ordine di inserimento — verifica con `Album.objects.get(pk=5)`.

### Query 4 — Canzoni dei Queen ordinate per traccia

```python
Canzone.objects.filter(album__artista__nome='Queen').values('titolo', 'durata_secondi').order_by('album__anno', 'traccia')
```

Tre concetti usati insieme:
- `album__artista__nome`: traversata di due FK (`Canzone → Album → Artista`)
- `.values('titolo', 'durata_secondi')`: restituisce dizionari invece di oggetti, con solo i campi specificati
- `.order_by('album__anno', 'traccia')`: ordina prima per anno dell'album, poi per numero di traccia

Output atteso:
```
<QuerySet [
  {'titolo': 'Bohemian Rhapsody', 'durata_secondi': 354},
  {'titolo': "You're My Best Friend", 'durata_secondi': 170},
  {'titolo': "Don't Stop Me Now", 'durata_secondi': 209},
  {'titolo': 'Fat Bottomed Girls', 'durata_secondi': 252}
]>
```

### Query 5 — Aggiorna disponibile con update()

```python
Album.objects.filter(anno__lt=1970).update(disponibile=False)
```

`.update()` esegue un singolo `UPDATE` SQL senza caricare gli oggetti in memoria — molto più efficiente di un loop. Restituisce il numero di righe aggiornate.

`anno__lt=1970` significa "anno minore di 1970" (`lt` = less than).

Output atteso: `4`

Gli album aggiornati sono: `Kind of Blue` (1959), `A Love Supreme` (1965), `Sgt. Pepper's` (1967), `Abbey Road` (1969).

---

## 8. Tabella dei metodi ORM

| Metodo | Cosa fa | Esempio |
|---|---|---|
| `.all()` | Restituisce tutti gli oggetti | `Album.objects.all()` |
| `.filter()` | Filtra per condizione | `Album.objects.filter(genere='Rock')` |
| `.get()` | Restituisce un solo oggetto | `Album.objects.get(pk=5)` |
| `.order_by()` | Ordina il risultato | `.order_by('-anno')` → decrescente |
| `.count()` | Conta il numero di risultati | `Canzone.objects.filter(album__pk=5).count()` |
| `.update()` | Aggiorna in una sola query senza caricare oggetti | `Album.objects.filter(anno__lt=1970).update(disponibile=False)` |
| `.values()` | Restituisce dizionari invece di oggetti | `.values('titolo', 'durata_secondi')` |
| `Q()` | Condizioni OR / AND complesse | `filter(Q(genere='Rock') \| Q(genere='Jazz'))` |
| `__` (traversata FK) | Naviga le relazioni tra modelli | `album__artista__nome` |
| `__gt` | Maggiore di | `filter(anno__gt=2000)` |
| `__lt` | Minore di | `filter(anno__lt=1970)` |
| `__in` | Valore in una lista | `filter(nome__in=["Coltrane", "Davis"])` |
| `__icontains` | Contiene (case insensitive) | `filter(nome__icontains='queen')` |
