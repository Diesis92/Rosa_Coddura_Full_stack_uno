from django.urls import path
from .import views

app_name ='ecommerce'

urlpatterns = [
    path(
        'acquisto/',
        views.acquisto_prodotto,
        name = 'acquisto_prodotto'
    ),

    path(
            'conferma/',
            views.conferma_acquisto,
            name = 'conferma_acquisto'
    ),

    path(
            'catalogo/',
            views.catalogo_prodotti,
            name = 'catalogo_prodotti'
    )
]
