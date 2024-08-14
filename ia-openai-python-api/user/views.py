# users/views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import CustomUser
from .serializers import UserSerializer, UserSerializerDetail
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


@api_view(['GET'])
def getAll(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getById(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    serializer = UserSerializerDetail(user)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = UserSerializerDetail(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    serializer = UserSerializerDetail(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patch(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    serializer = UserSerializerDetail(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteById(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Auhentication login and register :v

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        return Response({"message": "Login successful", "success": True, }, status=200)
    else:
        return Response({"message": "Invalid username or password", "success": False}, status=200)

