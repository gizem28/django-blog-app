from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password, **extra_fields):

        if not email:
            raise ValueError('Email is mandatory')
        # if not username:
        #     raise ValueError('Users must have a username')
        username=self.get_username(username)
        email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        # CustomUser.objects.create_superuser(username='admin', password = 'admin123', is_superuser = False)

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, null=True, unique=True)
    email = models.EmailField('email address', null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    # is_superuser is defined at PermissionsMixin
    # password and last_login defined at AbstractBaseUser

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username