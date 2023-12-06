from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
//user, content, timestamp, likes

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="item")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"comment on post,{self.post}, by {self.comment_by}"
