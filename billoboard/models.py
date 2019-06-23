from django.contrib.gis.db import models
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from datetime import datetime    

class Thread(models.Model):
    title = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    last_edit = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.ForeignKey(get_user_model(), 
    related_name='thread_owner', 
    on_delete=models.CASCADE, 
    db_index=True)

class ThreadComments(models.Model):
    owner = models.ForeignKey(get_user_model(), 
        related_name='thread_comment_owner', 
        on_delete=models.CASCADE, 
        db_index=True)
    thread = models.ForeignKey(Thread, 
        related_name='comment_thread', 
        on_delete=models.CASCADE, 
        db_index=True)
    parent = models.ForeignKey('self', 
            on_delete=models.CASCADE,
            null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)