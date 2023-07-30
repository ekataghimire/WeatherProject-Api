from django.contrib import admin
from django.urls import path, include
from weather_api.views import fetch_weather_data, get_weather_data

urlpatterns = [
    path('', fetch_weather_data, name='fetch_weather_data'), 
    path('get_weather_data', get_weather_data, name='get_weather_data'),
    path('admin/', admin.site.urls),
    path('api/', include('weather_api.urls')),
]
