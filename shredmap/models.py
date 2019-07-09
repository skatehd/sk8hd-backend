from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from datetime import datetime    
from django.core.validators import MinValueValidator, MaxValueValidator

class Location(models.Model):
    created_by = models.ForeignKey(get_user_model(),
        null=True, 
        related_name='location_owner', 
        on_delete=models.SET_NULL, 
        db_index=True)
    location = models.PointField()
    name = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)


class LocationComments(models.Model):
    owner = models.ForeignKey(get_user_model(), 
        related_name='location_comment_owner', 
        on_delete=models.CASCADE, 
        db_index=True)
    location = models.ForeignKey(Location, 
        related_name='comments', 
        on_delete=models.CASCADE, 
        db_index=True)
    parent = models.ForeignKey('self', 
            on_delete=models.CASCADE,
            null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)


class Images(models.Model):
    owner = models.ForeignKey(get_user_model(), 
        related_name='location_image_owner', 
        on_delete=models.CASCADE, 
        db_index=True)
    location = models.ForeignKey(Location, 
        related_name='images', 
        on_delete=models.CASCADE, 
        db_index=True)
    image = models.ImageField()
    date = models.DateTimeField(default=datetime.now, blank=True)

class Tricks(models.Model):
    owner = models.ForeignKey(get_user_model(), 
        related_name='location_trick_owner', 
        on_delete=models.CASCADE, 
        db_index=True)
    location = models.ForeignKey(Location, 
        related_name='tricks', 
        on_delete=models.CASCADE, 
        db_index=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    trick = models.TextField()

class Ratings(models.Model):
    owner = models.ForeignKey(get_user_model(), 
        related_name='location_rating_owner', 
        on_delete=models.CASCADE, 
        db_index=True)
    location = models.ForeignKey(Location, 
        related_name='ratings', 
        on_delete=models.CASCADE, 
        db_index=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        unique_together = ('owner', 'location',)


class SkateObjects(models.Model):
    owner = models.ForeignKey(get_user_model(),
        null = True, 
        related_name='location_object_owner', 
        on_delete=models.SET_NULL, 
        db_index=True)
    location = models.ForeignKey(Location, 
        related_name='skateobjects', 
        on_delete=models.CASCADE, 
        db_index=True)
    name = models.TextField(max_length=128)
