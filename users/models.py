from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date

class User(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(('email address'), unique = True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    
    USERNAME_FIELD = 'username'
    
    def __str__(self):
	    return self.username
