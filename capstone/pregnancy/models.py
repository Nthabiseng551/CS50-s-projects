from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
    pregnant = models.BooleanField(default=False)
    dietician = models.BooleanField(default=False)
    counsellor = models.BooleanField(default=False)
    week_of_pregnancy =

    def __str__(self):
        return f"{self.user}, {self.week_of_pregnancy}"
