from pyexpat import model
from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    year = models.FloatField()
    director = models.CharField(max_length=40)
    actors = models.CharField(max_length=80)
    description = models.CharField(max_length=300)
    


