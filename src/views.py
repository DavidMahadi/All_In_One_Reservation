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
    elif request.method == 'DELETE': 
         VarHotel.delete() 
         return Response({'message': 'Hotel was deleted successfully!'})
     
@api_view(['GET','POST'])
def RoomModel(request):
    if request.method=='GET':
        VarRoom=Room.objects.all()
        serializer=RoomSerializer(VarRoom,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
@api_view(['GET','PUT','DELETE'])
def RoomDelete(request,pk):
    try:
        VarRoom=Room.objects.get(pk=pk)
    except:
        return Response("no valid data")
    if request.method=='GET':
        serializer=RoomSerializer(VarRoom)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=RoomSerializer(VarRoom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE': 
         VarRoom.delete() 
         return Response({'message': 'Hotel was deleted successfully!'}) 
     
     
@api_view(['GET','POST'])
def BookedHotelModel(request):
    if request.method=='GET':
        VarBook=BookedHotel.objects.all()
        serializer=BookHotelSerializer(VarBook,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=BookHotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data) 
    
@api_view(['GET','PUT','DELETE'])
def BookDelete(request,pk):
    try:
        VarBook=BookedHotel.objects.get(pk=pk)
    except:
        return Response("no valid data")
    if request.method=='GET':
        serializer=BookHotelSerializer(VarBook)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=BookHotelSerializer(VarBook,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE': 
         VarBook.delete() 
         return Response({'message': 'Hotel was deleted successfully!'})
     
@api_view(['GET','POST'])
def  DriverModel(request):
    if request.method=='GET':
        VarDriver= Driver.objects.all()
        serializer=DriverSerializer(VarDriver,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET','POST','DELETE'])
def DriverModelDelete(request,pk):
    try:
        VarDrive=Driver.objects.get(pk=pk)
    except:
        return Response("no valid data")
    if request.method=='GET':
        serializer=DriverSerializer(VarDrive)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=DriverSerializer(VarDrive,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='DELETE':
        VarDrive.delete()
        return Response({'message':'Driver was deleted succefuly!'})
        
        
@api_view(['GET','POST'])
def  UberModel(request):
    if request.method=='GET':
        VarUber= Uber.objects.all()
        serializer=UberSerializer(VarUber,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=UberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET','POST','DELETE'])
def UberModelDelete(request,pk):
    try:
        VarUber=Uber.objects.get(pk=pk)
    except:
        return Response("no valid data")
    if request.method=='GET':
        serializer=UberSerializer(VarUber)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=UberSerializer(VarUber,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='DELETE':
        VarUber.delete()
        return Response({'message':'Uber was deleted succefuly!'})
    
    
    
@api_view(['GET','POST'])
def  UberCarsModel(request):
    if request.method=='GET':
        VarUberCars= UberCars.objects.all()
        serializer=UberCarsSerializer(VarUberCars,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=UberCarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
@api_view(['GET','POST','DELETE'])
def UberCarsModelDelete(request,pk):
    try:
        VarUberCars=UberCars.objects.get(pk=pk)
    except:
        return Response("no valid data")
    if request.method=='GET':
        serializer=UberCarsSerializer(VarUberCars)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=UberCarsSerializer(VarUberCars,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='DELETE':
        VarUberCars.delete()
        return Response({'message':'UberCar was deleted succefuly!'})
        
                 
    
@api_view(['GET','POST'])
def  BookedUberModel(request):
    if request.method=='GET':
        VarBookedUber= BookedUber.objects.all()
        serializer=BookedUberSerializer(VarBookedUber,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=BookedUberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
@api_view(['GET','POST','DELETE'])
def BookedUberModelDelete(request,pk):
    try:
        VarBookedUber=BookedUber.objects.get(pk=pk)
    except:
        return Response("no valid data")
    if request.method=='GET':
        serializer=BookedUberSerializer(VarBookedUber)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=BookedUberSerializer(VarBookedUber,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='DELETE':
        VarBookedUber.delete()
        return Response({'message':'BookedUber was deleted succefuly!'})
        


