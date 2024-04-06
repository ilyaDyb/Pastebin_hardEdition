from datetime import datetime
from celery import shared_task
from django.core.cache import cache
from django.utils import timezone

from posts.models import Post

@shared_task
def cache_popular_posts():
    try:
        popular_posts = Post.objects.filter(views__gt=10)
        for post in popular_posts:
            hash = post.postmeta.hash_id
            cache.add(key=hash, value=post)
    except Exception as ex:
        return ex

@shared_task
def delete_old_posts():
    current_date = timezone.now()
    try:
        Post.objects.filter(when_del__lt=current_date).delete()
        return "Success"
    except Exception as ex:
        return str(ex)