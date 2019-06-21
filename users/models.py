# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
User = get_user_model()

class UserProfile(models.Model):
    profile = models.ImageField(null=True, blank=True, upload_to='profile/')
    user = models.OneToOneField(User, related_name="info", on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if not self.profile
    #         im = Image.open(self.profile)
    #         # remove image if it exists

    #         output = BytesIO()
    #         im = im.resize( (256 , 256) )

    #         im.save(output, format='JPEG', quality=100)
    #         output.seek(0)

    #     self.profile = InMemoryUploadedFile(output,'ImageField', str(self.user.id) + ".jpg" , 'image/jpeg', 
    #     sys.getsizeof(output), None)
    #     super(UserProfile,self).save(*args, **kwargs)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
         UserProfile.objects.create(user=instance)


