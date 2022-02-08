from django.urls import path, include
from .views import register, user_logout, user_login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register' ),
    path('logout/', user_logout, name='logout' ),
    path('login/', user_login, name='user_login' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/',
    auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
    ),
]