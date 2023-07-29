# weather_api/urls.py

from django.urls import path
from .views import fetch_weather_data, get_weather_data

urlpatterns = [
    path('fetch_weather_data/', fetch_weather_data, name='fetch_weather_data'),
    path('weather/list/', get_weather_data, name='get-weather-data-list'),
]
