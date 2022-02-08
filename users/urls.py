from django.urls import path, include
from .views import register, user_logout, user_login
from django.contrib.auth import views as auth_views
from django.contrib.auth import views

urlpatterns = [
    path('register/', register, name='register' ),
    path('logout/', user_logout, name='logout' ),
    path('login/', user_login, name='user_login' ),
    path('accounts/', include('django.contrib.auth.urls')),
    # path(
    #     "password_change/done/",
    #     views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]