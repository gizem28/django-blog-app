from django.urls import path, include
from .views import PostCreateView, PostListView, PostDetailView, PostDeleteView, PostUpdateView, LikeView, AddCommentView


urlpatterns = [
    path('newblog/', PostCreateView, name='newblog'),
    path('', PostListView.as_view(), name='list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('update/<int:pk>/', PostUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name="delete"),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('detail/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]