from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, EventComments
from .serializers import EventSerializer, EventDetailSerializer, EventCommentSerializer
from rest_framework import generics
from django.utils import timezone
from rest_framework import permissions
from users.serializers import UserSerializer

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Events
    """
    now = timezone.now()
    queryset = Event.objects.filter(starttime__gt=now).order_by('starttime')
    serializer_class = EventSerializer

class EventDetailViewSet(generics.RetrieveAPIView):
    """
    API Endpoint for a single Event
    """
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class EventCommentCreateListViewSet(generics.ListCreateAPIView):
    serializer_class = EventCommentSerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = None
           

    def get_queryset(self):
        event = self.kwargs['pk']
        return EventComments.objects.filter(event__id=event)

    def perform_create(self, serializer):
        event = self.kwargs['pk']
        serializer.save(owner=self.request.user, event_id=event)