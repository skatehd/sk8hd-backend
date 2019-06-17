from django.contrib import admin
from django.forms import ModelForm
from django import forms
from .models import Event, EventComments

# # This is to add the wisiwyg editor to the admin page
# class EventForm(ModelForm):
#     class Meta: 
#         model = Event
#         body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'starttime', 'endtime')
    fields = ('title', 'short_description', 'description', 'starttime', 'endtime', 'image')


admin.site.register(Event, EventAdmin)
admin.site.register(EventComments)