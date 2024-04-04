from Pastebin_hardEdition.celery import app
from django.core.cache import cache

from posts.models import Post


@app.task
def cache_popular_posts():
    try:
        popular_posts = Post.objects.filter(views__gt=10)
        for post in popular_posts:
            hash = post.postmeta.hash_id
            cache.add(key=hash, value=post)
    except Exception as ex:
        return ex
    
# @app.task в планах
# def async_updateDataForCacheAndDb():
#     ...