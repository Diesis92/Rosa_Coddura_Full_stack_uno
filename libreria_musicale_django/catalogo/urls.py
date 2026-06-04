from django.urls import path
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import views

app_name = 'catalogo'  # ← mancava

urlpatterns = [
    path('',                      views.home,                    name='home'),
    path('artisti/',              views.artista_list,            name='artista-list'),
    path('albums/',               views.album_list,              name='album-list-fbv'),
    path('album/<int:album_id>/', views.album_detail,            name='album-detail'),
    path('redirect/',             views.redirect_home,           name='redirect-home'),
    path('albums/list/',          views.AlbumListView.as_view(), name='album-list-cbv'),
    path("albums/<int:pk>/",views.AlbumDetailView.as_view(),     name="album-detail"),
    path('dashboard/',login_required(views.DashboardView.as_view()), name='dashboard'),
]