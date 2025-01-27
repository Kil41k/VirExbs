from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

from .models import User
from .forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

def profile(request):
    return render(request, 'users/profile.html')

def logout(request):
    auth.logout(request)
    return redirect('/')