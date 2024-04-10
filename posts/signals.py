import hashlib
import logging

from django.dispatch import receiver
from django.db.models.signals import post_save

from posts.tasks import create_notifications

from posts.models import Post, PostMeta

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Post)
def create_post_meta(sender, instance, created, **kwargs):
    if created:
        print("Signal triggered for post:", instance.id)
        post_id = instance.id
        hash_id = hashlib.md5(str(post_id).encode()).hexdigest()

        PostMeta.objects.create(post=instance, hash_id=hash_id)
        #notifications
        create_notifications.delay(post_id=instance.id)