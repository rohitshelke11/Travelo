from django.db import models
from django_google_maps import fields as map_fields

# Create your models here.
class destination(models.Model):

    destination_id = models.IntegerField(primary_key='destination_id')
    name = models.CharField(max_length=100)
    des = models.TextField()
    img = models.ImageField(upload_to='destinations')
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
    g = geocoder.mapbox(self.address, key=mapbox_access_token)
    g = g.latlng  # returns => [lat, long]
    self.lat = g[0]
    self.long = g[1]
    return super(destination, self).save(*args, **kwargs)

    
class places(models.Model):

    place_id = models.IntegerField(primary_key='place_id')
    destination_id = models.IntegerField(foregin)
    name = models.CharField(max_length=100)
    des = models.TextField()
    img = models.ImageField(upload_to='places')
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
    g = geocoder.mapbox(self.address, key=mapbox_access_token)
    g = g.latlng  # returns => [lat, long]
    self.lat = g[0]
    self.long = g[1]
    return super(Address, self).save(*args, **kwargs)
