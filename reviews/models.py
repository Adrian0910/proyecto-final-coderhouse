from django.db import models


class Reviews(models.Model):
    Name = models.CharField(max_length=40)
    Rating  = models.FloatField()
    Review= models.CharField(max_length=500)
   