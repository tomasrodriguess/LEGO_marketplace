from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        user = User.objects.filter(id=self.request.user.id).first()
        return user
    
    def update(self, request, *args, **kwargs):
        user = self.request.user
        new_email = request.data.get('email')

        if new_email:
            user.email = new_email
            user.save()
            return Response({'detail': 'Email updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email field is required'}, status=status.HTTP_400_BAD_REQUEST)
        
#ROUTE BELLOR TO RESET PASSWORD