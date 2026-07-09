from django.urls import path
from .views import lista_libri, dettaglio_libro


urlpatterns = [

    path(
        "libri/",
        lista_libri
    ),

    path(
        "libri/<int:id>/",
        dettaglio_libro
    ),

]