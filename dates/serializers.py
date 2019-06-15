from rest_framework import serializers
from .models import Event, EventComments
from users.serializers import UserProfileSerializer
from django.contrib.auth import get_user_model
from django.conf import settings

class EventDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Event
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Event
        fields = ('id', 'title', 'short_description', 'starttime', 'endtime', 'image')

class EventCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='get_user_model')
    event = serializers.ReadOnlyField(source='Event')

    class Meta: 
        model = EventComments
        fields = ('__all__')

    def get_user_model():
        return owner
        