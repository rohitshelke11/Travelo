from django.db import models
from django.db.models import Avg
import geocoder 

mapbox_access_token = 'pk.eyJ1Ijoic2FoaWxzaGFpa2gxNjM0IiwiYSI6ImNrdXV2eTVvZTFoMnIydmxuaXFia3kxYXcifQ.HALeRa9ddGCfM85eJA8GpA'
# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    des = models.TextField()
    img = models.ImageField(upload_to='destinations')
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Destination, self).save(*args, **kwargs)

class Place(models.Model):

    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    des = models.TextField()
    img = models.ImageField(upload_to='place')
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def average_rating(self) -> float:
        return Review.objects.filter(place=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.name}: {self.average_rating()}"
       
    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Place, self).save(*args, **kwargs)
    


class Review(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    des = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.place.name}: {self.user_name}"