from django.contrib.gis.db import models
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from datetime import datetime    

class Event(models.Model):
    title = models.TextField()
    short_description = models.TextField()
    description = HTMLField()
    starttime = models.DateTimeField(auto_now=False, auto_now_add=False)    
    endtime = models.DateTimeField(auto_now=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)


class EventComments(models.Model):
    owner = models.ForeignKey(get_user_model(), 
        related_name='comment_owner', 
        on_delete=models.CASCADE, 
        db_index=True)
    event = models.ForeignKey(Event, 
        related_name='comment_event', 
        on_delete=models.CASCADE, 
        db_index=True)
    parent = models.ForeignKey('self', 
            on_delete=models.CASCADE,
            null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)