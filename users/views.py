from django.shortcuts import render
from .serializers import UserProfileSerializer
from rest_framework import generics
from .models import UserProfile

# Create your views here.
class UserDetailViewSet(generics.RetrieveAPIView):
    """
    API Endpoint for retrieving users
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer