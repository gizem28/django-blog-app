from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from main.settings import LOGIN_REDIRECT_URL
from django.http import HttpResponseRedirect
from hitcount.views import HitCountDetailView

@login_required()
def PostCreateView(request):
    model = Blog
    form=BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            return redirect("list")
            success_message =('Blog added successfully.')
    context = {"form":form}  
    return render(request, "blog/post_create.html", context)

    
class PostListView(ListView):
    template_name='blog/post_list.html'
    model=Blog
    context_object_name='blogs'

class PostDetailView(HitCountDetailView):
    model=Blog
    template_name='blog/blog_detail.html'
    slug_field='slug'
    count_hit=True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff=get_object_or_404(Blog, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        context["total_likes"] =total_likes
        return context
    
class PostUpdateView(UpdateView):
    model=Blog
    form_class=BlogForm
    template_name='blog\post_update.html'
    success_url=reverse_lazy('list')
    
    
class PostDeleteView(DeleteView):
    model=Blog
    template_name='blog\post_delete.html'
    success_url=reverse_lazy('list')
    
def LikeView(request, pk):
    post=get_object_or_404(Blog, id=request.POST.get('blog_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='blog/add_comment.html'
    
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url=reverse_lazy('list')
    