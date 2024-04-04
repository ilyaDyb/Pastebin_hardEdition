import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pastebin_hardEdition.settings")

app = Celery("Pastebin_hardEdition")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


#beats
app.conf.beat_schedule = {
    'cache-popular-post&Meta-every-30-seconds': {
        'task': 'tasks.cache_popular_posts',
        'schedule': 30.0,
    },
}
app.conf.timezone = 'UTC'

# app.conf.beat_schedule = {    В планах
#     'async_update-Data-For-Cache-And-Db': {
#         'task': 'tasks.async_updateDataForCacheAndDb',
#         'schedule': 60.0,
#     },
# }
