from rest_framework import serializers
from .models import Location, Images, Tricks, Ratings, LocationComments, SkateObjects
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.conf import settings


class LocationSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Location
        fields = ('id', 'location', 'name')


class CommentViewSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta: 
        model = LocationComments
        fields = "__all__"

class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = LocationComments
        fields = ('parent', 'content', )
    

class ImageViewSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta: 
        model = Images
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Images
        fields = "__all__"

class TricksViewSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta: 
        model = Tricks
        fields = "__all__"

class SkateObjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SkateObjects
        fields = ('name', )

# class RatingsViewSerializer(serializers.ModelSerializer):
#     average = 
#     count = 

#     class Meta: 
#         model = Ratings
#         fields = ('average', 'count')

class LocationDetailSerializer(serializers.ModelSerializer):
    comments = CommentViewSerializer(many=True)
    images = ImageViewSerializer(many=True)
    tricks = TricksViewSerializer(many=True)
    skateobjects = SkateObjectSerializer(many=True)
    # ratings = RatingsViewSerializer(many=True)

    class Meta: 
        model = Location 
        fields = ('location', 'name', 'comments', 'tricks', 'images', 'skateobjects')
