from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    names = models.CharField(max_length=255)
    lastnames = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'
