from django.urls import path, include
from .views import PostCreateView, PostListView, PostDetailView
# , post_delete, post_list, post_update

urlpatterns = [
    path('newblog/', PostCreateView.as_view(), name='newblog'),
    path('', PostListView.as_view(), name='list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="detail"),
]