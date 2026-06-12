from django.urls import re_path
from .views import place_order

urlpatterns = [
    re_path(
        r'^(?P<data>\d{4}-\d{2}-\d{2})/$',
        place_order.as_view(),
        name='articoli_per_data'
    ),
]