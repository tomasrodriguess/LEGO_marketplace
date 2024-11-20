from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Store, Listing
from .serializers import StoreSerializer
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class StoreCreateView(generics.CreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_moderator:
            raise PermissionDenied("Only moderators can create stores.")

        serializer.save()