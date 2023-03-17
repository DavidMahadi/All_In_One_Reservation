from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register',views.register),
    path('login',views.login),
    path('bookairplaneticket',views.Flight_customer),
    path('bookairplaneticketdetails',views.Flight_customer_details),
    # path('bookairplaneticketdetails',views.BookAirPlaneTicketdetails),
    # path('bookhotel',views.HotelReservation),
    # path('bookhotel',views.HotelReservationdetails),
    # path('bookuber',views.UberReservation),
    # path('bookuberdetails',views.UberReservationdetails),
    # path('booktour',views.Tour),
    # path('booktourdetails',views.Tourdetails),
]