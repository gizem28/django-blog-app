from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.contrib.auth.models import User
from PIL import Image

class User(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(('email address'), unique = True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    
    USERNAME_FIELD = 'username'
    
    def __str__(self):
	    return self.username

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.png', upload_to='profile_pics' )

    def __str__(self):
	    return f'{self.user.username} Profile'
 
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        
        if img.height >300 or img.width >300:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
        