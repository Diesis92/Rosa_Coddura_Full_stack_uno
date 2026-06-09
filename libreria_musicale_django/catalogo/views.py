# # ── django.http ────────────────────────────────────────────────────────────────
# from django.http import (
#     HttpResponse,           # risposta HTML grezza — 200
#     JsonResponse,           # risposta JSON — 200
#     HttpResponseRedirect,   # reindirizzamento — 302
#     HttpResponseBadRequest, # richiesta malformata — 400
#     HttpResponseNotFound,   # risorsa non trovata — 404
#     HttpResponseNotAllowed, # metodo HTTP non permesso — 405
#     HttpResponseServerError # errore interno — 500
# )

# # ── django.shortcuts ───────────────────────────────────────────────────────────
# from django.shortcuts import (
#     render,              # renderizza un template HTML
#     redirect,            # reindirizza a un URL o a un name
#     get_object_or_404,   # get() + 404 automatico se non esiste
#     get_list_or_404      # filter() + 404 automatico se lista vuota
# )

# # ── django.views ───────────────────────────────────────────────────────────────
# from django.views import View                    # CBV base

# # ── django.views.generic ───────────────────────────────────────────────────────
# from django.views.generic import (
#     ListView,    # lista oggetti
#     DetailView,  # dettaglio singolo oggetto
#     CreateView,  # form creazione
#     UpdateView,  # form modifica
#     DeleteView   # form cancellazione
# )

# # ── django.views.decorators.http ───────────────────────────────────────────────
# from django.views.decorators.http import (
#     require_http_methods,  # @require_http_methods(["GET", "POST"])
#     require_GET,           # solo GET
#     require_POST           # solo POST
# )

# # ── models ─────────────────────────────────────────────────────────────────────
# from .models import Artista, Album, Canzone


# def home(request):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])
#     return HttpResponse("<h1>Benvenuto nella Libreria Musicale</h1>")


# def artista_list(request):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])

#     artisti = Artista.objects.all()

#     data = []
#     for artista in artisti:
#         data.append({
#             'id': artista.id,
#             'nome': artista.nome
#         })

#     return JsonResponse(data, safe=False)


# def album_list(request): #togliere la logica for perché è una cosa che si mette sul template. Qua non serve la logica
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])

#     albums = Album.objects.all()

#     data = []
#     for album in albums:
#         data.append({
#             'id': album.id,
#             'titolo': album.titolo,
#             'artista': album.artista.nome,
#             'anno': album.anno
#         })
#     return JsonResponse(data, safe=False)
    
# #CBV 
# # class AlbumListView(View):
# #     def get(self, request):
# #         albums = Album.objects.all()

# #        context = {
# #             'albums': albums
# #         }
# #        return render(request, 'album_list.html', context)

# class AlbumListView(View):
#     def get(self, request):
#         albums = Album.objects.all()
#         context = {
#             'albums': albums
#         }
#         return render(request, 'album_list.html', context)

# def album_detail(request, album_id):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])

#     try:
#         album = Album.objects.get(id=album_id)
#     except Album.DoesNotExist:
#         return HttpResponseBadRequest("Album non trovato")

#     return JsonResponse({
#         'id': album.id,
#         'titolo': album.titolo,
#         'artista': album.artista.nome,
#         'anno': album.anno
#     })


# def redirect_home(request):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])

#     return HttpResponseRedirect('/catalogo/')


# ----------------------------------------------------------------------------------
#applicare il decoratore @login_required alle view che richiedono autenticazione, ad esempio:


from django.http import (
    HttpResponse,
    JsonResponse,
    HttpResponseRedirect,
    HttpResponseNotAllowed,
)

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST, require_http_methods
from django.views import View

from django.views.generic import DetailView

#dalla shell django
# python manage.py shell
# >>> from django.views.generic import DetailView
# >>> import inspect
# >>> inspect.getmro(DetailView)
# (<class 'django.views.generic.detail.DetailView'>, <class 'django.views.generic.detail.SingleObjectTemplateResponseMixin'>, 
#  <class 'django.views.generic.base.TemplateResponseMixin'>, <class 'django.views.generic.detail.BaseDetailView'>, 
#  <class 'django.views.generic.detail.SingleObjectMixin'>, <class 'django.views.generic.base.ContextMixin'>, <class 'django.views.generic.base.View'>, <class 'object'>)

from .models import Artista, Album, Commento


# ─────────────────────────────────────────────
# FUNZIONI BASE
# ─────────────────────────────────────────────

# def home(request):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])
#     return HttpResponse("<h1>Benvenuto nella Libreria Musicale</h1>")

# def homepage(request):
#     return render(request, 'catalogo/homepage.html')


def artista_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    artisti = Artista.objects.all()
    data = [{'id': a.id, 'nome': a.nome} for a in artisti]
    return JsonResponse(data, safe=False)


def album_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    albums = Album.objects.all()
    data = [{
        'id': a.id,
        'titolo': a.titolo,
        'artista': a.artista.nome,
        'anno': a.anno
    } for a in albums]

    return JsonResponse(data, safe=False)


def album_detail(request, album_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    album = get_object_or_404(Album, id=album_id)

    return JsonResponse({
        'id': album.id,
        'titolo': album.titolo,
        'artista': album.artista.nome,
        'anno': album.anno,
    })


def redirect_home(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    return HttpResponseRedirect('/catalogo/')




class AlbumListView(View):
    def get(self, request):
        albums = Album.objects.all()
        return render(request, 'catalogo/album_list.html', {
            'albums': albums
        })


class AlbumDetailView(View):
    def get(self, request, pk):
        album = get_object_or_404(Album, id=pk)
        return render(request, 'catalogo/album_detail.html', {
            'album': album
        })




@login_required(login_url='/accounts/login/')
def profilo_utente(request):
    return render(request, 'catalogo/profilo.html', {
        'utente': request.user
    })


#mixin
#form django.core.expceptions import PermissionDenied
#from django.contrib.auth.mixins import AccessMixin
# class LoginRequiredMixin(AccessMixin):
#     """Verifica che l'utente sia autenticato, altrimenti reindirizza alla pagina di login."""
#     def dispatch(self, request, *args, **kwargs):#intercetta tutte le richieste (GET, POST, ecc.) e verifica l'autenticazione prima di delegarla ai metodi della view (get, post, ecc.)
#         if not request.user.is_authenticated: #controlla se l'utente è autenticato. Se non lo è, chiama handle_no_permission() che di default reindirizza alla pagina di login.
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs) #se l'utente è autenticato, chiama il metodo dispatch() della classe base (AccessMixin) che a sua volta chiama il metodo dispatch() della view originale (ad esempio, AlbumListView) che gestisce la richiesta normalmente.


#loginrequiredMixin è una classe che estende AccessMixin e implementa il metodo dispatch() per verificare l'autenticazione dell'utente. Puoi usarla come mixin nelle tue view basate su classi per proteggere l'accesso alle pagine che richiedono autenticazione. Ad esempio:
#class DashboardView(LoginRequiredMixin, View):
#    def get(self, request):
#        login_url = '/accounts/login/' #puoi specificare l'URL di login se diverso da quello di default
#        return render(request, 'dashboard.html')

#permissionRequiredMixin è simile a LoginRequiredMixin ma verifica anche i permessi specifici dell'utente oltre all'autenticazione. Puoi usarlo per proteggere l'accesso a pagine che richiedono permessi specifici, ad esempio:
# from django.contrib.auth.mixins import PermissionRequiredMixin
# class AdminView(PermissionRequiredMixin,  UpdateView):
# permission_required = ['catalogo.change_album'] #specifica i permessi richiesti per accedere alla view (in questo caso, il permesso di modificare un album)
#     model = Album
#     fields = ['titolo', 'artista', 'anno']
#     template_name = 'catalogo/admin.html'


#UserPassesTestMixin è un mixin che permette di definire una logica personalizzata per verificare se un utente ha accesso a una view. Devi implementare il metodo test_func() che restituisce True se l'utente ha accesso e False altrimenti. Ad esempio:
# from django.contrib.auth.mixins import UserPassesTestMixin
# class StaffOnlyView(UserPassesTestMixin, ListView):
#     def test_func(self):
# #         return self.request.user.is_staff #verifica se l'utente è staff (puoi definire la logica che preferisci, ad esempio controllare un gruppo o un attributo personalizzato)
#       def handle_no_permission(self):
#             return HttpResponseRedirect('/accounts/login/') #puoi personalizzare la risposta in caso di accesso negato, ad esempio reindirizzando alla pagina di login o mostrando un messaggio di errore


#AccessMixin è la classe base per i mixin di accesso (come LoginRequiredMixin e PermissionRequiredMixin) che fornisce il metodo handle_no_permission() per gestire le richieste non autorizzate. Non è pensata per essere usata direttamente, ma puoi estenderla per creare mixin personalizzati se necessario.
# class MyCustomAccessMixin(View):
#     def dispatch(self, request, *args, **kwargs):
#         if not self.check_custom_condition(request.user): #definisci la tua logica personalizzata per verificare l'accesso (ad esempio, controllare un attributo dell'utente o una condizione specifica)
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)


#ContextMixin è un mixin che fornisce il metodo get_context_data() per aggiungere dati al contesto del template. Puoi usarlo per passare dati comuni a tutte le view che lo estendono, ad esempio:
#SingleObjectMixin è un mixin che fornisce il metodo get_object() per recuperare un singolo oggetto dal database in base a un identificatore (ad esempio, pk o slug) passato nella URL. Puoi usarlo nelle view di dettaglio per semplificare il recupero dell'oggetto, ad esempio:

#esempio ContextMixin e SingleObjectMixin:

# from django.views.generic import TemplateView
# from django.views.generic.base import ContextMixin

# class HomepageView(ContextMixin, TemplateView):
#     template_name = 'catalogo/homepage.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['message'] = 'Benvenuto nella Libreria Musicale!' #aggiunge un messaggio al contesto che sarà disponibile nel template
#         return context
    
# #SingleObjectMixin è un mixin che fornisce il metodo get_object() per recuperare un singolo oggetto dal database in base a un identificatore (ad esempio, pk o slug) passato nella URL. Puoi usarlo nelle view di dettaglio per semplificare il recupero dell'oggetto, ad esempio:
# from django.views.generic import View
# from django.views.generic.detail import SingleObjectMixin
# from catalogo.models import Album

# class AlbumDetailView(SingleObjectMixin, View):
#     model = Album
#     template_name = 'catalogo/album_detail.html'

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object() #recupera l'oggetto specifico (ad esempio, un album) utilizzando il metodo get_object() fornito da SingleObjectMixin che si basa sul modello e sull'identificatore passato nella URL
#         return HttpResponse(f"Dettagli dell'album: {self.object.titolo}") #renderizza il template con il contesto preparato e restituisce la risposta HTTP
    
# #mulipleObjectMixin è un mixin che fornisce il metodo get_queryset() per recuperare una lista di oggetti dal database in base a un modello e a eventuali filtri. Puoi usarlo nelle view di lista per semplificare il recupero degli oggetti, ad esempio:
# from django.views.generic import View
# from django.views.generic.list import MultipleObjectMixin
# from catalogo.models import Album
# class AlbumListView(MultipleObjectMixin, View):
#     model = Album
#     template_name = 'catalogo/album_list.html'
#     ordering = ['titolo'] #opzionale, specifica l'ordinamento degli oggetti recuperati (ad esempio, per titolo in ordine alfabetico)

#     def get(self, request, *args, **kwargs):
#         self.object_list = self.get_queryset() #recupera la lista di oggetti (ad esempio, tutti gli album) utilizzando il metodo get_queryset() fornito da MultipleObjectMixin che si basa sul modello e su eventuali filtri
#         return HttpResponse(f"Lista degli album: {[album.titolo for album in self.object_list]}") #renderizza il template con il contesto preparato e restituisce la risposta HTTP


#mixin per Form ed editing

#FormMixin è un mixin che fornisce il supporto per la gestione dei form nelle view basate su classi. Fornisce metodi per gestire la visualizzazione del form, la validazione dei dati e il salvataggio dell'oggetto associato al form. Puoi usarlo nelle view di creazione e modifica per semplificare la gestione dei form, ad esempio:
#django.views.generic.edit
#form_class = AlbumForm #specifica la classe del form da utilizzare per la creazione o modifica dell'album (deve essere definita in forms.py)
#initial = {'titolo': 'Titolo di default'} #opzionale, specifica i valori iniziali da precompilare nel form (ad esempio, un titolo di default)
#success_url = '/catalogo/albums/' #opzionale, specifica l'URL di successo a cui reindirizzare dopo la creazione o modifica dell'album (può essere una URL o un name)
#get_form() = un metodo che restituisce un'istanza del form da utilizzare nella view, ad esempio:
# def get_form(self, form_class=None):
#     if form_class is None:
#         form_class = self.get_form_class() #recupera la classe del form specificata nella view (ad esempio, AlbumForm)
#     return form_class(**self.get_form_kwargs()) #restituisce un'istanza
#form_valid() = un metodo che viene chiamato quando il form è valido
#form_invalid() = un metodo che viene chiamato quando il form non è valido

# #esempio completo di FormMixin:
# from django.views.generic.edit import View
# from django.views.generic.edit import FormMixin
# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)

# class ContactView(FormMixin, View):
#     form_class = ContactForm
#     template_name = 'contact.html'
#     success_url = '/catalogo/contact/'

#     def get(self, request, *args, **kwargs):
#         form = self.get_form() #ottiene un'istanza del form da visualizzare
#         return  self.render(self.get_context_data, (form=form)) #renderizza il template con il form nel contesto

#     def post(self, request, *args, **kwargs):
#         form = self.get_form() #ottiene un'istanza del form con i dati POST
#         if form.is_valid(): #verifica se il form è valido
#             # qui puoi gestire i dati del form (ad esempio, inviare un'email o salvare un messaggio)
#             return self.form_valid(form) #chiama il metodo form_valid() se il form è valido
#         else:
#             return self.form_invalid(form) #chiama il metodo form_invalid() se il form non è valido

#DeletionMixin è un mixin che fornisce il supporto per la gestione della cancellazione di un singolo oggetto nel modello. Fornisce metodi per gestire la visualizzazione della conferma di cancellazione e l'effettiva cancellazione dell'oggetto. Puoi usarlo nelle view di cancellazione per semplificare la gestione della cancellazione, ad esempio:
#from django.views.generic.edit import View
#from django.views.generic.edit import DeletionMixin
#from django.Http import HttpResponseRedirect

#ProcessFormView è un mixin che fornisce il supporto per la gestione dei form nelle view basate su classi, ma a differenza di FormMixin, ProcessFormView gestisce sia la visualizzazione del form che la sua elaborazione in un unico metodo post(). Puoi usarlo nelle view di creazione e modifica per semplificare la gestione dei form, ad esempio:
#from django.views.generic.edit import View
#from django.views.generic.edit import ProcessFormView
#from django import forms
#from django.Shortcuts import render,redirect

# class BasicForm(forms.Form):
#     data = forms.CharField(max_length=50)
# class MyCustomFormView(FormMixin, ProcessFormView, View):
#     form_class = BasicForm
#     template_name = 'custom_form.html'
#     success_url = '/done/'

#     def get(self, request, *args, **kwargs):
#         form = self.get_form() #ottiene un'istanza del form da visualizzare
#         return self.render(self.get_context_data(form=form)) #renderizza il template con il form nel contesto
#     def  form_valid(self, form):
#         print("Form valido, dati:", form.cleaned_data) #qui puoi gestire i dati del form (ad esempio, salvarli o inviare un'email)
#         return redirect(self.success_url) #reindirizza alla URL di successo dopo la gestione dei dati del form
#     def form_invalid(self, form):
#         print("Form non valido, errori:", form.errors) #qui puoi gestire gli errori del form (ad esempio, loggarli o mostrare un messaggio di errore)
#         return render(request, self.template_name,{'form': form}) #renderizza nuovamente il template con il form e gli errori nel contesto
    

# class BaseDetailView(View):#
#    def get(self,request, *args, **kwargs):
#        self.object = self.get_object() #recupera l'oggetto specifico (ad esempio, un album) utilizzando un metodo get_object() che deve essere definito nella view concreta (ad esempio, AlbumDetailView)
#        context = self.get_context_data(object=self.object) #prepara il contesto per il template, includendo l'oggetto recuperato
#        return self.render_to_response(context) #renderizza il template con il contesto preparato e restituisce la risposta HTTP

# class DetailView(SingleObjectTemplateResponseMixin, BaseDetailView):
#     """Vista che aggiunge il supporto per il recupero di un singolo oggetto e la renderizzazione di un template specifico. """
#     pass

#differenza tra decoratori e mixin: i decoratori sono funzioni che modificano il comportamento di una funzione o di un metodo, mentre i mixin sono classi che forniscono funzionalità aggiuntive a una classe esistente attraverso l'ereditarietà. I decoratori vengono applicati direttamente alle funzioni o ai metodi, mentre i mixin vengono utilizzati come classi base nelle view basate su classi per estendere le loro funzionalità.

@cache_page(60 * 10, key_prefix='homepage')
def homepage(request):
    return render(request, 'catalogo/homepage.html')




@require_POST
def elimina_commento(request, commento_id):
    commento = get_object_or_404(Commento, id=commento_id)
    commento.delete()
    return JsonResponse({'status': 'success'})




@method_decorator(login_required, name='dispatch')
@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class ReportView(View):

    def get(self, request):
        return render(request, 'report.html')

    def post(self, request):
        return render(request, 'report.html', {
            'message': 'POST ricevuto'
        })