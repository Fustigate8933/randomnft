from urllib.parse import urlparse
from django.urls import path
from .views import *

urlpatterns = [
    path('search/', SearchMarketPlace.as_view()),
    path('list/', ListImageLinks.as_view())
]
