from django.db import models

# Create your models here usando ORM di Django per definire la struttura del database per i prodotti del catalogo
class Prodotto(models.Model):
    nome = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    disponibile = models.BooleanField(default=True)
    creato_il = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    class Meta: #Metadati per il modello Prodotto, ad esempio per definire l'ordinamento predefinito
        ordering = ['-creato_il'] #asc e desc per ordinare i prodotti in base alla data di creazione, dal più recente al più vecchio
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"

# class Autore(models.Model):
#     nome = models.CharField(max_length=50)
#     cognome = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)

# class Articolo(models.Model):
#     titolo = models.CharField(max_length=100)
#     contenuto = models.TextField()
#     autore = models.ForeignKey('Autore', on_delete=models.CASCADE)
#     data_pubblicazione = models.DateTimeField(auto_now_add=True)

#forma abbreviata per creare un nuovo autore e un nuovo articolo usando il metodo create() del manager del modello, che consente di creare e salvare un'istanza in un'unica operazione
# nuovo_utente = Autore.objects.create(nome="Mario", cognome="Rossi", email="mario.rossi@example.com")
# nuovo_articolo = Articolo.objects.create(titolo="Un articolo di esempio", contenuto="Questo è il contenuto dell'articolo.", autore=nuovo_utente)
# update con pk=1
# Articolo.objects.filter(pk=1).update(titolo="Titolo aggiornato")
# delete con pk=1
# Articolo.objects.filter(pk=1).delete()   
# queryset per ottenere tutti gli articoli pubblicati da un autore specifico
# articoli_di_mario = Articolo.objects.filter(autore__nome="Mario", autore__cognome="Rossi")
# queryset per ottenere tutti gli articoli pubblicati in un intervallo di date specifico
# articoli_recenti = Articolo.objects.filter(data_pubblicazione__range=["2024-01-01", "2024-12-31"])
# queryset per ottenere tutti gli articoli che contengono una parola chiave specifica nel titolo o nel contenuto
# articoli_con_keyword = Articolo.objects.filter(Q(titolo__icontains="esempio") | Q(contenuto__icontains="esempio"))
# queryset per ottenere tutti gli articoli ordinati per data di pubblicazione in ordine decrescente
# articoli_ordinati = Articolo.objects.all().order_by('-data_pubblicazione
# queryset per ottenere tutti gli articoli pubblicati da un autore specifico e ordinati per data di pubblicazione in ordine decrescente
# articoli_di_mario_ordinati = Articolo.objects.filter(autore__nome="Mario", autore__cognome="Rossi").order_by('-data_pubblicazione')
# queryset per ottenere tutti gli articoli pubblicati da un autore specifico e ordinati per data di pubblicazione in ordine decrescente, limitando i risultati ai primi 5 articoli
# articoli_di_mario_ordinati_limitati = Articolo.objects.filter(autore__nome="Mario", autore__cognome="Rossi").order_by('-data_pubblicazione')[:5]
# queryset per ottenere tutti gli articoli pubblicati da un autore specifico e ordinati per data di pubblicazione in ordine decrescente, limitando i risultati ai primi 5 articoli e includendo solo i campi titolo e data_pubblicazione
# articoli_di_mario_ordinati_limitati_values = Articolo.objects.filter(autore__nome="Mario", autore__cognome="Rossi").order_by('-data_pubblicazione')[:5].values('titolo', 'data_pubblicazione')
# queryset per ottenere tutti gli articoli pubblicati da un autore specifico e ordinati per data di pubblicazione in ordine decrescente, limitando i risultati ai primi 5 articoli e includendo solo i campi titolo e data_pubblicazione, restituendo i risultati come dizionari invece che come istanze del modello
# articoli_di_mario_ordinati_limitati_values_list = Articolo.objects.filter(autore__nome="Mario", autore__cognome="Rossi").order_by('-data_pubblicazione')
# [:5].values_list('titolo', 'data_pubblicazione')
# queryset per ottenere tutti gli articoli pubblicati da un autore specifico e ordinati per data di pubblicazione in ordine decrescente, limitando i risultati ai primi 5 articoli e includendo solo i campi titolo e data_pubblicazione, restituendo i risultati come tuple invece che come istanze del modello o dizionari
# articoli_di_mario_ordinati_limitati_values_list_tuples = Articolo.objects.filter(autore__nome="Mario", autore__cognome="Rossi").order_by('-data_pubblicazione')[:5].values_list('titolo', 'data_pubblicazione')
#  
