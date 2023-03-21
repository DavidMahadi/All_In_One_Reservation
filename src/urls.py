from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *


urlpatterns = [
    path('hotelPost/',HotelModel,name='getHotel'),
    path('hotelDelete/<int:pk>',HotelModelDelete,name='deleteHotel'),
    
]