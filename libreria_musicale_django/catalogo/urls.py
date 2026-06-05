from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('artisti/', views.artista_list),
    path('albums/', views.album_list),
    path('album/<int:album_id>/', views.album_detail),
    path('dashboard/', views.ReportView.as_view()),
]

#per il login usare quello dell'admin