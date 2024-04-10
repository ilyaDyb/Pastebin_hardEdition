from django.db import models

from users.models import User
from posts.models import Post

class Notifications(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="notifications")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "Notifications"

    def __str__(self):
        return f"Notification for {self.user.username}"
    