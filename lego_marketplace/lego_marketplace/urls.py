from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('sets/', include('lego_sets.urls')),
    path('collection/', include('collection.urls')),
    path('marketplace/', include('marketplace.urls')),
]
