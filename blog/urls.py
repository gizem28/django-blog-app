from django.urls import path, include
from .views import PostCreateView, PostListView, PostDetailView, PostDeleteView, PostUpdateView


urlpatterns = [
    path('newblog/', PostCreateView.as_view(), name='newblog'),
    path('', PostListView.as_view(), name='list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('update/<int:pk>/', PostUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name="delete"),
]