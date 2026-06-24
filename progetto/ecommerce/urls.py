from django.urls import path
from . import views

app_name = "ecommerce"

urlpatterns = [
    # catalogo (homepage)
    path('', views.CatalogoProdottiView.as_view(), name='home'),

    # catalogo prodotti
    path('catalogo/', views.CatalogoProdottiView.as_view(), name='catalogo_prodotti'),

    # dettaglio prodotto
    path('prodotto/<int:pk>/', views.ProdottoDetailView.as_view(), name='prodotto_detail'),

    # crea prodotto
    path('prodotto/add/', views.ProdottoCreateView.as_view(), name='prodotto_create'),

    # modifica prodotto
    path('prodotto/<int:pk>/edit/', views.ProdottoUpdateView.as_view(), name='prodotto_update'),

    # elimina prodotto
    path('prodotto/<int:pk>/delete/', views.ProdottoDeleteView.as_view(), name='prodotto_delete'),

    # acquisto
    path('acquisto/', views.acquisto_prodotto, name='acquisto_prodotto'),

    # conferma acquisto
    path('conferma/', views.conferma_acquisto, name='conferma_acquisto'),

    # categorie (CBV corretta)
    path('categorie/', views.CategoriaListView.as_view(), name='categorie'),
]