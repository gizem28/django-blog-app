from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms
from django.contrib.auth.models import User
class UserForm(UserCreationForm):
    # image=forms.ImageField()
    # bio=forms.CharField()
 
    class Meta():
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = [ 'username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
     class Meta():
        model = Profile
        fields = ['image', 'bio']
        