from django.contrib.auth.models import User
from django.db import models


class Enthusiast(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='enthusiast')
    city = models.CharField(max_length=255)
