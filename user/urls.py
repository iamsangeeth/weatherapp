from django.urls import path 
from user.views import * 
 
urlpatterns = [ 
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('details', UserView.as_view())
]
