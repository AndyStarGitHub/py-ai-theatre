from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login

from accounts.forms import CustomUserCreationForm

User = get_user_model()


def signup_view(request: HttpResponse) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # або в чат
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
