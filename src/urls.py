from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *


urlpatterns = [
    path('register',views.register),
    path('login',views.login),
    path('changetype',views.changeType),
    
    path('hotelPost/',HotelModel,name='getHotel'),
    path('hotelDelete/<int:pk>',HotelModelDelete,name='deleteHotel'),

    path('hotelPost/',HotelModel,name='getHotel'),
    path('hotelDelete/<int:pk>',HotelModelDelete,name='deleteHotel'),

    path('hotelPost/',HotelModel,name='getHotel'),
    path('hotelDelete/<int:pk>',HotelModelDelete,name='deleteHotel'),

    path('hotelPost/',HotelModel,name='getHotel'),
    path('hotelDelete/<int:pk>',HotelModelDelete,name='deleteHotel'),
    
]