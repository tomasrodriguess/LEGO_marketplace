from django.urls import path
from .views import StoreCreateView, StoreListView,StoreDetailView,ListingCreateView,ListingDetailView,ListingListView

urlpatterns = [
    path('store', StoreCreateView.as_view(),name='create_store'),
    path('store/search', StoreListView.as_view(),name='list_stores'),
    path('store/<str:id>', StoreDetailView.as_view(),name='get_Store'),
    path('listing', ListingCreateView.as_view(),name='create_listing'),
    path('listing/search', ListingListView.as_view(),name='list_listings'),
    path('listing/<str:id>', ListingDetailView.as_view(),name='get_listing'),
    
]