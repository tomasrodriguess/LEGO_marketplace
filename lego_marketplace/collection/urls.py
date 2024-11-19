from django.urls import path
from .views import CollectionCreateView,CollectionListView, CollectionDetailView, CollectionItemCreateView

urlpatterns = [
    path('', CollectionListView.as_view(),name='list'),
    path('create', CollectionCreateView.as_view(),name='create'),
    path('add_item', CollectionItemCreateView.as_view(), name='add-collection-item'),
    path('<str:id>', CollectionDetailView.as_view(),name='get')
]