from django.db import models

# Create your models here.

class AirPlaneTicket(models.Model):
    Fullnames=models.CharField(max_length=100)
    PassportDetails=models.CharField(max_length=100,default=0)
    Traveltime=models.DateField()
    FlightAirline=models.CharField(max_length=200)
    FlightClass=models.CharField(max_length=200)
    PaymentInformation=models.IntegerField(default=0)
    
    def __str__(self):
        return self.Fullnames
    
    
    
class HotelReservation(models.Model):
    Fullnames=models.CharField(max_length=100)
    HotelName=models.CharField(max_length=200)
    CheckIn=models.DateField()
    CheckOut=models.DateField()
    NumberOfPeaple=models.IntegerField(default=0)
    NumberOfRooms=models.IntegerField(default=0)
    
    def __str__(self):
        return self.Fullnames
    
    
    
class UberReservation(models.Model):
    Fullnames=models.CharField(max_length=200,default=0)
    PickUpLocation=models.CharField(max_length=200,default=0)
    DropoffLocation=models.CharField(max_length=200,default=0)
    pickUpDate=models.DateField()
    pickUpTime=models.TimeField()
    
    def __str__(self):
        return self.Fullnames
    
    
    
class Tour(models.Model):
    Fullnames=models.CharField(max_length=200,default=0)
    TourDate=models.DateField()
    TourCampany=[
        ('Gorilla Rwanda Tour'),
        ('Best Safari Tour'),
        ('SilverBack gorilla Tour'),
        
    ]
    
    
    def __str__(self):
         return self.Fullnames