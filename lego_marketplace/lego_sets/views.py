from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import LegoSet
from .serializers import LegoSetSerializer
from rest_framework.exceptions import PermissionDenied

# List all Lego sets and create new ones (moderators only)
class LegoSetListView(generics.ListAPIView):
    queryset = LegoSet.objects.all()
    serializer_class = LegoSetSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = LegoSet.objects.all()
        name = self.request.query_params.get('name', None)
        set_number = self.request.query_params.get('set_number', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if set_number:
            queryset = queryset.filter(set_number__icontains=set_number)

        return queryset

class LegoSetCreateView(generics.CreateAPIView):
    serializer_class = LegoSetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only moderators can create Lego sets.")
        serializer.save(created_by=self.request.user)

class LegoSetDetailView(generics.RetrieveAPIView):
    queryset = LegoSet.objects.all()
    serializer_class = LegoSetSerializer
    permission_classes = [AllowAny]
    lookup_field ='set_number'
