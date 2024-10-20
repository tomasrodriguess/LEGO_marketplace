from django.urls import path
from .views import LegoSetListView, LegoSetCreateView, LegoSetDetailView

urlpatterns = [
    path('', LegoSetListView.as_view(),name='list'),
    path('create', LegoSetCreateView.as_view(),name='create'),
    path('<str:set_number>', LegoSetDetailView.as_view(),name='get'),
]