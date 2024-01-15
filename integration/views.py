from django.shortcuts import render
from rest_framework.exceptions import status
from rest_framework.views import APIView, Response
from .accuweather import AccuWeather
from .utils import saveSearchData

class FindCitiesView(APIView):
    
    ''' View to fetch city/location suggestion list with text search '''
    
    def get(self, request):
        query = request.GET.get('query', None)
        if query:
            cities = AccuWeather().findCities(query)
            return Response(cities, status=200)
    
class WeatherDetails(APIView):
    
    ''' View to fetch daily forcast details with locationkey '''
    
    def get(self, request):
        query = request.GET.get('locationKey', None)
        if query:
            forcast_data = AccuWeather().dailyForecast(query)
            return Response(forcast_data, status=200)

class CurrentWeather(APIView):

    ''' View to fetch current weather conditions with locationkey '''

    def get(self, request):
        query = request.GET.get('locationKey', None)
        if query:
            current_data = AccuWeather().currentCondition(query)
            if type(current_data) == list and len(current_data) > 0:
                current_data = current_data[0]
                #saving search return for historical analytics
                saveSearchData(request.user, query, current_data)
            else:
                current_data = {}
            return Response(current_data, status=200)
