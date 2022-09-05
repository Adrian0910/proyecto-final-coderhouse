from django.db import models

class Tv_shows(models.Model):
    image = models.ImageField(upload_to='tv_shows/', null=True, blank=True)
    name = models.CharField(max_length=40)
    price = models.FloatField()
    year = models.IntegerField()
    director = models.CharField(max_length=40)
    actors = models.CharField(max_length=80)
    description = models.CharField(max_length=300)