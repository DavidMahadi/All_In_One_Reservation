from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *


urlpatterns = [
    path('hotelPost/',HotelModel,name='getHotel'),
    path('hotelDelete/<int:pk>',HotelModelDelete,name='deleteHotel'),
    path('RoomModel/',RoomModel,name='getroom'),
    path('RoomDelete/<int:pk>',RoomDelete,name='deleteroom'),
    path('DriverModel/',DriverModel,name='gellalldrivers'),
    path('DriverModelDelete/<int:pk>',DriverModelDelete,name='deleteDriver'),
    path('UberModel/',UberModel,name='UberModel'),
    path('UberModelDelete/<int:pk>',UberModelDelete,name='UberModelDelete'),
    path('UberCarsModel/',UberCarsModel,name='UberCarsModel'),
    path('UberCarsModelDelete/<int:pk>',UberCarsModelDelete,name='UberCarsModelDelete'),
    path('BookedUberModel/',BookedUberModel,name='BookedUberModel'),
    path('BookedUberModelDelete/<int:pk>',BookedUberModelDelete,name='BookedUberModelDelete'), 
       
]