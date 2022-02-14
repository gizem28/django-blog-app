from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
# add authenticate and login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import UserUpdateForm, ProfileUpdateForm

class AboutView(TemplateView):
    template_name="users/about.html"

def register(request):
    form=UserForm
    if request.method=='POST':
        form=UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Your account has been created!")
            return redirect("login")
    context = {
        "form_user" : form
    }
    return render(request, "users/register.html", context)

def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return render(request, "users/user_logout.html")

def user_login(request):

    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Login successfull")
            login(request, user)
            return redirect('list')
    return render(request, 'users/user_login.html', {"form": form})


def password_change(request):
    if request.method == 'POST':
        # We will use user change form this time
        # Import it
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
    else:
        form = UserChangeForm()
    
    context = {
        'form': form
    }
    
    return render(request, "users/password_change.html", context)


@login_required
def profile(request):
    if request.method == 'POST':
      u_form=UserUpdateForm(request.POST, instance=request.user)
      p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
      if u_form.is_valid() and p_form.is_valid():
          u_form.save()
          p_form.save()
          messages.success(request, "Your account has been updated!")
          return redirect('profile')
    else:
       u_form=UserUpdateForm(instance=request.user)
       p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    
    return render(request, "users/profile.html", context)