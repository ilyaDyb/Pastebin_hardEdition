from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from posts.models import Post

from datetime import datetime, timedelta

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        when_del = request.POST["expiry_date"]
        print(when_del)
        Post.objects.create(title=title, user=request.user, text=content, when_del=when_del)
        messages.success(request, "You successfully created a post")
        return redirect(reverse("main:index"))
    else:
        current_date = datetime.now()
        default_expiry_date = current_date + timedelta(days=3)
        context = {"default_expiry_date": default_expiry_date.strftime("%Y-%m-%d")}
        return render(request, "posts/create_post.html", context=context)
    

def post_detail(request, hash_id):
    post = cache.get(key=hash_id)
    if post is None:
        post = Post.objects.get(postmeta__hash_id=hash_id)
        post.increment_views()
    else:
        post.increment_views()
    context = {"post": post}
    return render(request, "posts/post.html", context=context)