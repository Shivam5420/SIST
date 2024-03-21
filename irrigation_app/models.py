from django.db import models

# Create your models here.
from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    depth = models.CharField(max_length=50)
    moisture = models.FloatField()
    temperature = models.FloatField()

class WeatherData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    weather_description = models.CharField(max_length=100)

class Crop(models.Model):
    name = models.CharField(max_length=100)
    water_needs = models.FloatField()
