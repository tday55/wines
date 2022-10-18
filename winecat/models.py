from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from datetime import datetime


class Maker(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class Location(models.Model):
    def __str__(self):
        return self.room + ', ' + self.level + ', ' + self.slot
    room = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    slot = models.CharField(max_length=50)
    
class Wine(models.Model):
    def __str__(self):
        return self.appellation + ', ' + self.maker.name +', ' + self.year + ', ' + self.blend
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    wine_type = models.CharField(max_length=200)
    blend = models.CharField(max_length=200)
    appellation = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    link = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200)
    alcohol = models.CharField(max_length=200)
    where = models.ForeignKey(Location, on_delete=models.CASCADE)
    acquired = models.DateTimeField('date acquired')
    def how_old_is_it(self):
        return timezone.now().year - int(self.year)
    
class Stock(models.Model):
    def __str__(self):
        return self.wine.maker.name
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    vintage = models.IntegerField('Vintage', default=0)
    acquired = models.DateTimeField('date acquired')
    alcohol = models.CharField(max_length=200, default='NA')
    where = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    opened = models.DateTimeField('date opened', blank=True)
    
