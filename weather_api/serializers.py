# weather_api/serializers.py
from rest_framework import serializers
from .models import WeatherData

# converting WeatherData model instances into JSON or XML format and use it for responses in your Django REST Framework views.

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
