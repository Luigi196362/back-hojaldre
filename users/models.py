from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address=models.TextField(blank=True)
    is_admin = models.BooleanField(default=False,null=False)
