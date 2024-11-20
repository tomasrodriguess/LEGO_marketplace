from django.urls import path
from .views import StoreCreateView

urlpatterns = [
    path('store', StoreCreateView.as_view(),name='create'),
]