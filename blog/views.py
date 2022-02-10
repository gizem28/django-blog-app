from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from main.settings import LOGIN_REDIRECT_URL

class PostCreateView(SuccessMessageMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name="blog/post_create.html"
    success_url= reverse_lazy('list')
    success_message =('Blog added successfully.')
    
class PostListView(ListView):
    template_name='blog/post_list.html'
    model=Blog
    context_object_name='blogs'
    
# @login_required(login_url=LOGIN_REDIRECT_URL)
class PostDetailView(DetailView):
    if not user.is_authenticated:
        reverse_lazy('login')
    model=Blog