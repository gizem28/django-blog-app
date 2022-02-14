from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.png', upload_to='profile_pics' )
    bio=models.TextField(max_length=500, blank=True)
    
    def __str__(self):
	    return f'{self.user.username} Profile'

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        
        if img.height >300 or img.width >300:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)