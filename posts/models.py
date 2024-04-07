from django.utils import timezone
from django.db import models
from users.models import User



class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None)
    text = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    when_del = models.DateTimeField()


    class Meta:
        db_table = 'Posts'
    

    def __str__(self) -> str:
        return self.title

    def increment_views(self):
        self.views += 1
        self.save()

class PostMeta(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    hash_id = models.CharField()
    class Meta:
        db_table = 'Posts_meta'

    def __str__(self):
        return self.hash_id
    