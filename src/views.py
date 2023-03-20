from django.http import JsonResponse
from .models import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from knox.auth import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.shortcuts import render



# Create your views here.
@api_view(['GET','POST'])
def Hotel(request):
    if request.method =='GET':
        hotel=Hotel.objects.all()
        serializer= HotelSerializer(customer, many=True)
        return Response({"hotel":serializer.data})

    if request.method =='POST':
        serializer=HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def Flight_customer_details(request, id):
    try:
        customer=AirPlaneTicket.objects.get(pk=id)

    except customer.DoesNotExist:
        return Response(status=satus.HTTP_401_NOT_FOUND)

    if request.method =='GET':
        serializer= BookAirPlaneTicketSerializer(customer)  
        return Response(serializer.data)


    elif request.method =='PUT':        
        serializer= BookAirPlaneTicketSerializer(customer, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)

    elif request.method=="DELETE":
        customer.delete()
        return Response("Delete Successful", status=status.HTTP_204_CONTENT)



@api_view(['POST'])
def register(request):
    serializer = RegisterUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _,token = AuthToken.objects.create(user)


    return Response({
        "user_infos": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        },
        # "token":token,
        "message": "Account Created Sucessfully."
        })


@api_view(["POST"])
def login(request):
    serializer= AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user= serializer.validated_data['user']

    _,token=AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
        },
        'token':token
        })