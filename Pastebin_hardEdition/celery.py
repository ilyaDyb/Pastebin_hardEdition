import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pastebin_hardEdition.settings")


app = Celery("Pastebin_hardEdition")
app.config_from_object(settings, namespace="CELERY")


tasks_module = 'posts.tasks'

# Добавляем путь к модулю с задачами
app.autodiscover_tasks([tasks_module])

# beats
app.conf.beat_schedule = {
    'cache-popular-post&Meta-every-30-seconds': {
        'task': 'posts.tasks.cache_popular_posts',
        'schedule': 30.0,
        'name': 'posts.tasks.cache_popular_posts',
    },
    'delete_old_posts_every_3hour': {
        'task': 'posts.tasks.delete_old_posts',
        'schedule': crontab(hour="*/3"),
        'name': 'posts.tasks.cdelete_old_posts',
    },
}



app.conf.timezone = 'UTC'


