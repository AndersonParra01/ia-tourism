# tourism/models.py
from django.db import models
from user.models import CustomUser

class TouristPlace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.TextField()
    location = models.CharField(max_length=100)
    users = models.ManyToManyField(CustomUser, related_name='places')

    class Meta:
        db_table = 'tourist_places'
