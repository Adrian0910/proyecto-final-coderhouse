from django.db import models


class Reviews(models.Model):
    name = models.CharField(max_length=40)
    rating  = models.FloatField()
    review= models.CharField(max_length=500)
    image = models.ImageField(upload_to='reviews/', null=True, blank=True)
   