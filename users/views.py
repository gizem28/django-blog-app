from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
# add authenticate and login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'users/base.html')

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
            return redirect("base")
    context = {
        "form_user" : form
    }
    return render(request, "users/register.html", context)

def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return redirect('base')

def user_login(request):

    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Login successfull")
            login(request, user)
            return redirect('base')
    return render(request, 'users/user_login.html', {"form": form})