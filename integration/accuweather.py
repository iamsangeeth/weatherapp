from django.conf import settings
import requests

class AccuWeather():
    def __init__(self):
        self.apikey = settings.ACCUWEATHER_API_KEY

    def findCities(self, query):
        url = 'http://dataservice.accuweather.com/locations/v1/cities/search?q={}'.format(query)
        r = requests.get(url, {'apikey': self.apikey})
        res = r.json()
        return res

    def dailyForecast(self, locationKey):
        url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{}'.format(locationKey)
        r = requests.get(url, { 'apikey': self.apikey, 'metric': True })
        return r.json()

    def currentCondition(self, locationKey):
        url = 'http://dataservice.accuweather.com/currentconditions/v1/{}'.format(locationKey)
        r = requests.get(url, { 'apikey': self.apikey })
        return r.json()
    
    @staticmethod
    def saveSearch(city, locationKey, data):
        return None
