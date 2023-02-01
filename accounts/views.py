from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def registrate_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                                     password=form.cleaned_data['password1'])
            return redirect('main_page')
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/registration_page.html", context={'form': form})


def sign_in_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"User {user.username} has been successfully logged in")
            return redirect('main_page')
        else:
            messages.error(request, "Username Or Password is incorrect!")
    return render(request, 'accounts/login_page.html')
