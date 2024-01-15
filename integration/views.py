from django.shortcuts import render
from rest_framework.exceptions import status
from rest_framework.views import APIView, Response
from .accuweather import AccuWeather

class FindCitiesView(APIView):
    def get(self, request):
        query = request.GET.get('query', None)
        if query:
            cities = AccuWeather().findCities(query)
            return Response(cities, status=200)
    
class WeatherDetails(APIView):
    def get(self, request):
        query = request.GET.get('locationKey', None)
        if query:
            forcast_data = AccuWeather().dailyForecast(query)
            return Response(forcast_data, status=200)

class CurrentWeather(APIView):
    def get(self, request):
        query = request.GET.get('locationKey', None)
        if query:
            current_data = AccuWeather().currentCondition(query)
            if current_data:
                current_data = current_data[0]
            return Response(current_data, status=200)