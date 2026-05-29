from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('artisti/', views.artista_list),
    path('albums/', views.album_list),
    path('album/<int:album_id>/', views.album_detail),
    path('redirect/', views.redirect_home),
]