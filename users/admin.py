from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('username', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)