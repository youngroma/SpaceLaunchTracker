from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.URLField(blank=True, null=True)

class FavoriteLaunch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    launch_id = models.CharField(max_length=100)
