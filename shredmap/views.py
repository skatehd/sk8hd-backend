from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Location, SkateObjects
from .serializers import LocationSerializer, LocationDetailSerializer, SkateObjectSerializer
from django.utils import timezone
from rest_framework import permissions
from datetime import datetime  
# Create your views here.


class LocationViewSet(generics.ListCreateAPIView):
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = None

    queryset = Location.objects.all()

    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class LocationDetailViewSet(generics.RetrieveAPIView):
    # TODO: reduce SQL calls by prefetching
    pagination_class = None
    queryset = Location.objects.all()

    serializer_class = LocationDetailSerializer


class SkateObjectViewSet(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = SkateObjects.objects.all()
    serializer_class = SkateObjectSerializer

    def perform_create(self, serializer):
        id = self.kwargs['pk']
        serializer.save(owner=self.request.user, location_id=id)