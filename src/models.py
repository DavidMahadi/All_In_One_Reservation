from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Hotel(models.Model):
    start_choice=(
        (1,'Three Start'),
        (2,'Four Start'),
        (3,'Five Start'),
        
    )
    name=models.CharField(max_length=100)
    sector=models.CharField(max_length=100) 
    district=models.CharField(max_length=100) 
    province=models.CharField(max_length=100) 
    stars=models.PositiveSmallIntegerField(choices=start_choice, default=1)
    working_hours=models.IntegerField()
    thumbnail=models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.name

class Room(models.Model):
    roomcapacity=(
        (1,'1 bed'),
        (2,'2 bed'),
        (3,'3 bed'),
        
    )
    
    price_choice=(
        (1,'1 bed/hour=100000'),
        (2,'2 bed/hour=200000'),
        (3,'3 bed/hour=300000'),
        
    )


    hotel:models.ForeignKey(Hotel,max_length=100, on_delete=models.CASCADE) 
    capacity=models.PositiveSmallIntegerField(choices=roomcapacity, default=1)
    thumbnail =models.ImageField()
    price_choices=models.PositiveSmallIntegerField(choices=price_choice, default=1)

    def __str__(self):
        return self.hotel

class BookedHotel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    def __str__(self):
        return self.user


class Driver(models.Model):
    name=models.CharField(max_length=200)
    tel=models.IntegerField()

    def __str__(self):
        return self.name


class Uber(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()

    def __str__(self):
        return self.name

class UberCars(models.Model):
    def price(self):
        price=self.workedhours * self.price_hour
        return price

    uber=models.ForeignKey(Uber,on_delete=models.CASCADE)
    plateno=models.IntegerField()
    seats=models.IntegerField()
    driver=models.ForeignKey(Driver,on_delete=models.CASCADE)
    workedhours=models.IntegerField()
    price_hour=models.FloatField(7000)
    payment=models.FloatField(default=price)

    def __str__(self):
        return self.uber

    

class BookedUber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Uber=models.ForeignKey(Uber,on_delete=models.CASCADE)
    def __str__(self):
        return self.user



class Plane(models.Model):
    company_choice=(
        (1,'RwandAir'),
        (2,'KenyanAir Ways'),
        (3,'EthiopianAir Ways'),
        (4,'EthiopianAir Ways'),
        (5,'EthiopianAir Ways'),
        (6,'EthiopianAir Ways')
        
    )
    ways=(
        (1,'one way'),
        (2,'Two Ways'),
        
    )

    TypeClass=(
        (1,'Business Class'),
        (2,'Economy Class'),
        
    )


    company=models.PositiveSmallIntegerField(choices=company_choice, default=1)
    travelway=models.PositiveSmallIntegerField(choices=ways, default=1)
    names=models.CharField(max_length=300)
    passport=models.IntegerField()
    classplane=models.PositiveSmallIntegerField(choices=TypeClass, default=1)
    Airport_departure=models.CharField(max_length=200)
    location_arrival=models.CharField(max_length=200)
    payment_info=models.CharField(max_length=300)

    def __str__(self):
        return self.company



class ChangeType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    certificate=models.ImageField(upload_to ='uploads/')
    def __str__(self):
        return self.user.first_name