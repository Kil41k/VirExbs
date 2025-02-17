import uuid

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse

from .models import User, EmailVerification
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from .tasks import send_email_verification


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
            user = form.save(commit=False)
            user.save()
            mail = EmailVerification.objects.create(user=user)
            send_email_verification.delay(user.id, mail.id)
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

def profile(request):
    return render(request, 'users/profile.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def delete_account(request):
    user = request.user
    user.delete()
    return redirect('articles:home')

def edit_acc(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:home')
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/edit_acc.html', {'form': form})


def EmailVerificationView(request, token):
    verification = get_object_or_404(EmailVerification, token=token)
    user = verification.user
    user.is_verificated = True
    user.save()
    return render(request, 'users/complete.html')



