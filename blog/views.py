from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class PostCreateView(SuccessMessageMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name="blog/post_create.html"
    success_url= reverse_lazy('base')
    success_message =('Blog added successfully.')