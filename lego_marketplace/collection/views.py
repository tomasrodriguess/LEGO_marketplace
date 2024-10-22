from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Collection, CollectionItem
from .serializers import CollectionSerializer, CollectionItemSerializer
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class CollectionCreateView(generics.CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Collection.objects.all()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
class CollectionDetailView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    
    def get_object(self):
        # Get the collection instance by pk
        collection = super().get_object()

        # Check if the collection is public or belongs to the current user
        if collection.public or collection.user == self.request.user:
            return collection
        else:
            # If neither, raise a permission denied error
            raise PermissionDenied("You do not have permission to view this collection.")