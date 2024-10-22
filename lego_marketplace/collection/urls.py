from django.urls import path
from .views import CollectionCreateView,CollectionListView, CollectionDetailView

urlpatterns = [
    path('', CollectionListView.as_view(),name='list'),
    path('create', CollectionCreateView.as_view(),name='create'),
    path('<str:id>', CollectionDetailView.as_view(),name='get'),
]