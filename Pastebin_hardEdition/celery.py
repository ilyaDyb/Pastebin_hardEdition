import os
from celery import Celery
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
}
app.conf.timezone = 'UTC'


# app.conf.beat_schedule = {    В планах
#     'async_update-Data-For-Cache-And-Db': {
#         'task': 'tasks.async_updateDataForCacheAndDb',
#         'schedule': 60.0,
#     },
# }