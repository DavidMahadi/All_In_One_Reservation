from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers, validators
from django.contrib.auth.password_validation import validate_password
        
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields=('id','name','sector',
            'district','province','stars','working_hours','thumbnail')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('id','hotel','capacity',
            'thumbnail','price_choices')

class BookHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookedHotel
        fields=('id','user','hotel')

class UberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Uber
        fields=('id','name','price')

class UberCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UberCars
        fields=('id','uber','plateno','seats','driver_name','driver_tel',
            'workedhours','price_hour','payment')

class BookedUberSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookedUber
        fields=('id','user','uber')

class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plane
        fields=('id','company','travelway','names','passport',
            'classplane','Airport_departure','location_arrival','payment_info')

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

class changeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    certificate = serializers.FileField()

    class Meta:
        model=ChangeType
        fields= [
            "id",
            "user",
            "certificate"
        ]