from django.db import models

# Create your models here.
class WeatherData(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    generationtime_ms = models.FloatField()
    utc_offset_seconds = models.IntegerField()
    timezone = models.CharField(max_length=100)
    timezone_abbreviation = models.CharField(max_length=10)
    elevation = models.FloatField()
    temperature_2m = models.JSONField()
    relativehumidity_2m = models.JSONField()
    windspeed_10m = models.JSONField()

    def __str__(self):
        return f"Weather Data for {self.latitude}, {self.longitude} at {self.generationtime_ms}"