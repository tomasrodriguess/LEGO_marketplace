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
        collection = super().get_object()
        if collection.public or collection.user == self.request.user:
            return collection
        else:
            raise PermissionDenied("You do not have permission to view this collection.")
        
class CollectionItemCreateView(generics.CreateAPIView):
    queryset = CollectionItem.objects.all()
    serializer_class = CollectionItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        collection = serializer.validated_data['collection']
        # Check if the user owns the collection
        if collection.user != self.request.user:
            raise PermissionDenied("You do not have permission to add items to this collection.")

        # Create the collection item
        serializer.save()