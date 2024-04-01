from django.shortcuts import render
from users.forms import UserRegistrationForm, UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        ...
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', context={'form': form})


def registration(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        ...
    else:
        form = UserLoginForm()
    return render(request, 'users/registration.html', context={'form': form})