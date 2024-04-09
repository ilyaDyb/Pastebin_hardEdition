from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from posts.models import Post

from users.models import User
from users.forms import UserRegistrationForm, UserLoginForm



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, "You successfuly sign in")
                return redirect(reverse("main:index"))
        messages.warning(request, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', context={'form': form})


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfuly sign up")
            return redirect(reverse("users:login"))

    else:
        form = UserLoginForm()
        
    return render(request, 'users/registration.html', context={'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))


@login_required
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(user=user).all()
    context = {"user": user, "posts":posts}
    return render(request, "users/profile.html", context=context)


def subscribe(request):
    if request.method == "POST":
        user_who_subscribe = request.user
        user_to_subscribe = User.objects.get(pk=request.POST["user_id_to_subscribe"])
        user_to_subscribe.subscribers.add(user_who_subscribe)
        messages.success(request, "You subscribed to this user")
        return JsonResponse({"status": "success"})
    else:
        return HttpResponse(status=404)