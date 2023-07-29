from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import WeatherData
from .serializers import WeatherDataSerializer
from django.urls import reverse

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
        # self.assertIn('message', response.data)
        # self.assertEqual(response.data['message'], "Weather data fetched and stored successfully.")
