from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, date

# Create your models here.
class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
    pregnant = models.BooleanField(default=False)
    dietician = models.BooleanField(default=False)
    counsellor = models.BooleanField(default=False)
    week_of_pregnancy = models.IntegerField(null=True)
    week_update_date = models.DateField(default=date.today)
    pre_weight = models.FloatField(null=True, blank=True)
    target_weight = models.FloatField(null=True, blank=True)
    current_weight = models.FloatField(null=True, blank=True)
    currentWeight_update_date = models.DateField(default=date.today)
    tests = models.ManyToManyField("Test", null=True, blank=True, related_name='usertests')

    def __str__(self):
        return f"{self.id}, {self.user}, {self.week_of_pregnancy}"

class Test(models.Model):
    test_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    trimester = models.IntegerField(null=True)
    done = models.BooleanField()

    def __str__(self):
        return f"{self.id},{self.done} {self.test_name}"
