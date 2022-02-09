from django.urls import path, include
from .views import PostCreateView
# , post_delete, post_list, post_update

urlpatterns = [
    path('post_create/', PostCreateView.as_view(), name='newblog')
]