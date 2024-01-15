from django.urls import path 
from .views import * 
 
urlpatterns = [ 
    path('location/search', FindCitiesView.as_view()),
    path('forecast', WeatherDetails.as_view()),
    path('currentcondition', CurrentWeather.as_view())
]
