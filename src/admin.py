from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(BookedHotel)
admin.site.register(Driver)
admin.site.register(Uber)
admin.site.register(UberCars)
admin.site.register(BookedUber)
admin.site.register(Plane)
admin.site.register(ChangeType)