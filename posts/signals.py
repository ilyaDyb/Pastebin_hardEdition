import hashlib

from django.dispatch import receiver
from django.db.models.signals import post_save


from posts.models import Post, PostMeta


@receiver(post_save, sender=Post)
def create_post_meta(sender, instance, created, **kwargs):
    if created:
        post_id = instance.id
        hash_id = hashlib.md5(str(post_id).encode()).hexdigest()

        PostMeta.objects.create(post=instance, hash_id=hash_id)