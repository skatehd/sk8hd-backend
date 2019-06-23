from rest_framework import serializers
from .models import Thread, ThreadComments
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.conf import settings


class ThreadSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta: 
        model = Thread
        fields = '__all__'

class ThreadWriteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Thread
        fields = ('title', 'content',)


class ThreadCommentSerializer(serializers.ModelSerializer):
    event = serializers.ReadOnlyField(source='Event')
    owner = UserSerializer()

    class Meta: 
        model = ThreadComments
        fields = ('id', 'parent', 'content', 'date', 'owner', 'event',)
    

class ThreadCommentWriteSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = ThreadComments
        fields = ('parent', 'content', )
    