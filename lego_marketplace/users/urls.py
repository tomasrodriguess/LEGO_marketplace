from django.urls import path, include
from .views import CreateUserView, UserProfileView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

urlpatterns = [
    path('register', CreateUserView.as_view(),name='register'),
    path('login', TokenObtainPairView.as_view(), name='get_token'),
    path('profile', UserProfileView.as_view(), name='user_profile'),
    path('update', UserProfileView.as_view(), name='update_user'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('api-auth/', include('rest_framework.urls')),
]