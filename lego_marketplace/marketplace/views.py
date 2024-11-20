from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Store, Listing
from .serializers import StoreSerializer, ListingSerializer
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

class StoreListView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Store.objects.all()
        name = self.request.query_params.get('name', None)

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    
class StoreDetailView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [AllowAny]
    lookup_field ='id'

class ListingCreateView(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not Store.objects.filter(user=self.request.user).exists():
            raise PermissionDenied({"User": "The specified user does not have a store."})
        serializer.save()

class ListingDetailView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]
    lookup_field ='id'

class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Listing.objects.all()
        set_number = self.request.query_params.get('set_number', None)
        if set_number:
            queryset = queryset.filter(lego_set=set_number)
        store = self.request.query_params.get('store', None)
        if store:
            queryset = queryset.filter(store=store)
        condition = self.request.query_params.get('condition', None)
        if condition:
            queryset = queryset.filter(condition=condition)
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset