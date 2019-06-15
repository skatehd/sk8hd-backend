from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile 

User = get_user_model()

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')


class UserSerializer(serializers.ModelSerializer):
    # TODO: add profile like https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta: 
        model = User
        fields = ('id', 'username')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta: 
        model = UserProfile
        fields = ('profile', 'user' )
    
    def to_representation(self, obj):
        """Move fields from user up one level."""
        representation = super().to_representation(obj)
        profile_representation = representation.pop('user')
        for key in profile_representation:
            representation[key] = profile_representation[key]

        return representation

class UserAddedInfoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserProfile
        fields = ('profile')

