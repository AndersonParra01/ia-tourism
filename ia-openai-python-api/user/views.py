# users/views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import CustomUser
from tourism.models import TouristPlace
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


@api_view(['POST'])
def add_users_to_place(request):
    try:
        place_id = request.data.get('place_id')
        user_ids = request.data.get('user_ids')

        if not place_id or user_ids is None:
            return Response({"error": "place_id y user_ids son requeridos."}, status=status.HTTP_400_BAD_REQUEST)

        place = get_object_or_404(TouristPlace, id=place_id)

        if not isinstance(user_ids, list):
            user_ids = [user_ids]

        place.users.add(*user_ids)

        return Response({"message": "Usuarios agregados exitosamente al lugar turístico."}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def remove_users_from_place(request):
    try:
        place_id = request.data.get('place_id')
        user_ids = request.data.get('user_ids')

        if not place_id or user_ids is None:
            return Response({"error": "place_id y user_ids son requeridos."}, status=status.HTTP_400_BAD_REQUEST)

        place = get_object_or_404(TouristPlace, id=place_id)

        if not isinstance(user_ids, list):
            user_ids = [user_ids]

        place.users.remove(*user_ids)

        return Response({"message": "Usuarios eliminados exitosamente del lugar turístico."}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
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
        user_data = {
            "id": user.id,
            "username": user.username,
            "names": user.names,
            "lastnames": user.lastnames,
        }
        return Response({
            "message": "Login successful",
            "success": True,
            "user": user_data
        }, status=200)
    else:
        return Response({
            "message": "Invalid username or password",
            "success": False
        }, status=200)