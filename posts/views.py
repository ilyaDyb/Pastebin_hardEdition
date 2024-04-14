from django.contrib import messages
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

from posts.models import Post

from datetime import datetime, timedelta

from posts.utils import q_search, util_for_sessions

@login_required
def create(request):
    if request.method == "POST":
        current_date = timezone.now().date()
        when_del_str = request.POST["expiry_date"]
        when_del = datetime.strptime(when_del_str, "%Y-%m-%d").date()

        if current_date >= when_del:
            messages.warning(request, "Invalid date")
            return redirect(reverse("posts:create"))

        elif int(str(when_del)[:3]) - int(str(current_date)[:3]) >= 1:
            messages.warning(request, "Very big date")
            return redirect(reverse("posts:create"))
        
        title = request.POST["title"]
        content = request.POST["content"]
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
    session_key = request.session.session_key
    if post is None:
        try:
            post = Post.objects.select_related('postmeta').get(postmeta__hash_id=hash_id)
            util_for_sessions(session_key, request, post)

        except Post.DoesNotExist:
            context = {"error_message": "Post not found"}
    else:
        util_for_sessions(session_key, request, post)
        cache.set(key=hash_id, value=post)

    context = {"post": post}
    return render(request, "posts/post.html", context=context)


def feed(request):
    page = request.GET.get("page", 1)
    filter = request.GET.get("filter", None)
    query = request.GET.get("q", None)
    posts = Post.objects.all()

    if filter == "popular":
        posts = posts.order_by("-views")
    elif filter == "new":
        posts = posts.order_by("created_at")
    elif filter == "old":
        posts = posts.order_by("-created_at")
    if query:
        posts = q_search(query=query)

    paginator = Paginator(posts, 5)
    current_page = paginator.page(int(page))
    context = {"posts": current_page}
    return render(request, "posts/feed.html", context=context)