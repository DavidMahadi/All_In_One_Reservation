from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Hotel,Room,BookedHotel,Driver,Uber,UberCars,BookedUber,Plane,ChangeType])
