from django.shortcuts import render
from rest_framework import viewsets
from .models import Thread, ThreadComments
from .serializers import ThreadCommentSerializer, ThreadCommentWriteSerializer, ThreadSerializer, ThreadWriteSerializer
from rest_framework import generics
from django.utils import timezone
from rest_framework import permissions
from datetime import datetime    

# Create your views here.

class ThreadViewSet(generics.ListCreateAPIView):
    """
    API Endpoints for Threads
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):        
        queryset = Thread.objects.all().order_by('-last_edit').select_related('owner').select_related('owner__info')
        search = self.request.query_params.get('q', None)
        if search is not None:
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return ThreadSerializer(*args, **kwargs)
        else: 
            return ThreadWriteSerializer(*args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ThreadCommentViewSet(generics.ListCreateAPIView): 
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = None
         
    def get_serializer(self, *args, **kwargs): 
        if self.request.method == 'GET':
            return ThreadCommentSerializer(*args, **kwargs)
        else: 
            return ThreadCommentWriteSerializer(*args, **kwargs)

    def get_queryset(self):
        id = self.kwargs['pk']
        return ThreadComments.objects.filter(thread__id=id).select_related('owner').select_related('owner__info')

    def perform_create(self, serializer):
        id = self.kwargs['pk']
        serializer.save(owner=self.request.user, thread_id=id)
        Thread.objects.filter(id=id).update(last_edit=datetime.now())