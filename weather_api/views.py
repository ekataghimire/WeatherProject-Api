from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
import requests
from .models import WeatherData
from .serializers import WeatherDataSerializer

class WeatherDataPagination(PageNumberPagination):
    page_size = 10  # Number of records per page
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['POST'])
def fetch_weather_data(request):
    #fetching the url
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    # exception handling 
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()
        api_data = response.json()

        # Save the data to the database using the WeatherData model
        weather_data = WeatherData(
            latitude=api_data['latitude'],
            longitude=api_data['longitude'],
            generationtime_ms=api_data['generationtime_ms'],
            utc_offset_seconds=api_data['utc_offset_seconds'],
            timezone=api_data['timezone'],
            timezone_abbreviation=api_data['timezone_abbreviation'],
            elevation=api_data['elevation'],
            temperature_2m=api_data['hourly']['temperature_2m'],
            relativehumidity_2m=api_data['hourly']['relativehumidity_2m'],
            windspeed_10m=api_data['hourly']['windspeed_10m'],
        )
        #saving the data in the database
        weather_data.save()

        # Paginate the saved data and return it in the response
        paginator = WeatherDataPagination()
        paginated_data = paginator.paginate_queryset(WeatherData.objects.all(), request)
        serializer = WeatherDataSerializer(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    # throwing exception if failed to fetch the data from the api
    except requests.exceptions.RequestException as e:
        return Response({"error": "Failed to fetch data from the API"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#get the database stored data in the view
@api_view(['GET'])
def get_weather_data(request):
    weather_data = WeatherData.objects.all()
    serializer = WeatherDataSerializer(weather_data, many=True)
    return Response(serializer.data)