from .models import User
from django.contrib.auth.forms import UserCreationForm
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ( 'username', 'email', 'password1', 'password2', 'profile_pic')
        # exclude = ('is_staff', 'is_active', 'date_joined', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', )
