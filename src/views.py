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


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def changeType(request):
    if request.method == 'POST':
        data = request.data 
        data['user'] = request.user.id
        print(data)
        serializer=changeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response("something goes wrong",status=status.HTTP_400_BAD_REQUEST)

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
         VarHotel.delete() 
         return Response({'message': 'Hotel was deleted successfully!'})
    
