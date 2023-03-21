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
def HotelModel(request):
    if request.method=='GET':
        VarHotel=Hotel.objects.all()
        serializer=HotelSerializer(VarHotel,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
@api_view(['GET','PUT','DELETE'])
def HotelModelDelete(request,pk):
    try:
        VarHotel=Hotel.objects.get(pk=pk)
    except:
        return Response("no valid data")
    if request.method=='GET':
        serializer=HotelSerializer(VarHotel)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=HotelSerializer(VarHotel,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
                
    
    


