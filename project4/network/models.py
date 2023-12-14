from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    post = models.CharField(max_length=300)
    post_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} by,{self.post_by}"

class UserFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")

    def __str__(self):
        return f"{self.following_user} is following {self.user}"

class PostLike(models.Model):
    likes = models.ManyToManyField(User, on_delete=models.CASCADE, related_name="post_like")

    def __str__(self):
        return self.likes.count()
