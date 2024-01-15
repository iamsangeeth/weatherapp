from django.conf import settings
import requests

class AccuWeather():

    '''
        Integration class for accuweather
    '''

    def __init__(self):
        self.apikey = settings.ACCUWEATHER_API_KEY

    def findCities(self, query):
        #fetches list of cities with query text
        url = 'http://dataservice.accuweather.com/locations/v1/cities/search?q={}'.format(query)
        r = requests.get(url, {'apikey': self.apikey})
        res = r.json()
        return res

    def dailyForecast(self, locationKey):
        #fetches daily forcast data with locationKey
        url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{}'.format(locationKey)
        r = requests.get(url, { 'apikey': self.apikey, 'metric': True })
        return r.json()

    def currentCondition(self, locationKey):
        #fetches current condition with locationKey
        url = 'http://dataservice.accuweather.com/currentconditions/v1/{}'.format(locationKey)
        r = requests.get(url, { 'apikey': self.apikey })
        return r.json()
 
