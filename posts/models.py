import datetime
from django.db import models
from users.models import User



class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    when_del = models.DateTimeField()
    class Meta:
        db_table = 'Posts'
    
    using = 'second_db'


class PostMeta(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    hash_id = models.CharField()
    class Meta:
        db_table = 'Posts_meta'