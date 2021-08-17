from django.db import models

# Create your models here.

class Movies(models.Model):
    userId = models.IntegerField()
    movieId = models.IntegerField()
    rating = models.FloatField()