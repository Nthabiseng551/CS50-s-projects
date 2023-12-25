from django.contrib import admin
from .models import User, UserProfile, Test, UserTest

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Test)
admin.site.register(UserTest)
