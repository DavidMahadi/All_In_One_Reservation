from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers, validators
from django.contrib.auth.password_validation import validate_password
        
class BookAirPlaneTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=AirPlaneTicket
        fields=('id','Fullnames','PassportDetails','Traveltime','FlightAirline','FlightClass','PaymentInformation')
        
    
class HotelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelReservation
        fields=('id','Fullnames','HotelName','CheckIn','CheckOut','NumberOfRooms')
        
class UberReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=UberReservation
        fields=('id','Fullnames','PickUpLocation','DropoffLocation','pickUpDate','pickUpTime')
     

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tour
        fields=('id','Fullnames','TourDate','TourCampany')
     


class RegisterUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
            )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {
            'required': True,
            'allow_blank': False,
            'validators': [
                validators.UniqueValidator(
                        User.objects.all(), "User with this email already exists"
                    )
            ]
            },
        }


    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password Fields didn't match"})

        return attrs


    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')


        user = User.objects.create(
            username = email,
            first_name = first_name,
            last_name = last_name,
            email = email
            )

        user.set_password(validated_data['password1'])
        user.save()


        return user