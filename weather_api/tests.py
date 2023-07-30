from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import WeatherData
from .serializers import WeatherDataSerializer
from django.urls import reverse

#this test case verifies that the "fetch_weather_data" API endpoint is working correctly and is able to fetch weather data from the external API and store it in the database.
class WeatherDataFetchTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_fetch_weather_data_endpoint(self):
        url = reverse('fetch_weather_data')
        print("Test URL:", url)
        response = self.client.post(url)
        print("Response status code:", response.status_code)
        print("Response data:", response.data)


        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertGreater(WeatherData.objects.count(), 0)
