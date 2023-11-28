from django.shortcuts import render
from rest_framework import generics

from users.models import CustomUser
from users.serializers import CustomUserSerializer

# Create your views here.

class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
