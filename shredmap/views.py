from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Location, SkateObjects, LocationComments, Images
from .serializers import LocationSerializer, LocationDetailSerializer, SkateObjectSerializer, CommentViewSerializer, CommentWriteSerializer, ImageSerializer
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


class LocationCommentViewSet(generics.ListCreateAPIView): 
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = None
         
    def get_serializer(self, *args, **kwargs): 
        if self.request.method == 'GET':
            return CommentViewSerializer(*args, **kwargs)
        else: 
            return CommentWriteSerializer(*args, **kwargs)

    def get_queryset(self):
        id = self.kwargs['pk']
        return LocationComments.objects.filter(location__id=id).select_related('owner').select_related('owner__info')

    def perform_create(self, serializer):
        id = self.kwargs['pk']
        serializer.save(owner=self.request.user, location_id=id)


class ImageUpload(generics.ListCreateAPIView):
   
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = ImageSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return Images.objects.filter(location__id=id)

    def perform_create(self, serializer):
        id = self.kwargs['pk']
        serializer.save(owner=self.request.user, location_id=id)

