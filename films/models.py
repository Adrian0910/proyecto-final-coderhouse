from pyexpat import model
from django.db import models

class Film(models.Model):
    #poster = models.ImageField(upload_to = 'posters/')
    name = models.CharField(max_length=40)
    price = models.FloatField()
    year = models.IntegerField()
    director = models.CharField(max_length=40)
    actors = models.CharField(max_length=80)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name



    

