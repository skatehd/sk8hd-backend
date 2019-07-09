from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.forms import ModelForm
from django import forms
from .models import Location, LocationComments, Images, Tricks, Ratings

# # This is to add the wisiwyg editor to the admin page
# class EventForm(ModelForm):
#     class Meta: 
#         model = Event
#         body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))


class LocationAdmin(OSMGeoAdmin):
    list_display = ('name', 'created_by', 'date',)
    fields = ('name', 'created_by', 'date', 'location')


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationComments)
admin.site.register(Images)
admin.site.register(Tricks)