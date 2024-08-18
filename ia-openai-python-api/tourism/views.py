import os
from django.shortcuts import get_object_or_404, render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import openai
from deep_translator import GoogleTranslator
from rest_framework import viewsets
from .models import TouristPlace
from .serializers import  TouristPlaceDetailWriteSerializer, TouristPlaceListSerializer, TouristPlaceReadSerializer
from rest_framework import status
from user.models import CustomUser

class TouristPlaceViewSet(viewsets.ModelViewSet):
    queryset = TouristPlace.objects.all()
    serializer_class = TouristPlaceListSerializer

def language_selector(language_code):
    # deep-translator no proporciona una lista de idiomas directamente,
    # así que verificamos manualmente algunos idiomas comunes.
    supported_languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'zh', 'ja', 'ru']
    if language_code not in supported_languages:
        raise ValueError(f"Language code '{language_code}' is not supported.")
    return language_code

@api_view(['POST'])
def get_completion(request):
    prompt = request.data.get('prompt')
    language = request.data.get('language', 'es')
    openai.api_key = settings.OPENAI_API_KEY

    try:
        if language == 'es':
            system_message = 'Eres un asistente útil especializado en turismo para Ecuador y respondes en español debes de ser lo mas claro y preciso en tus respuestas si mucho redondeo ve directo.'
        else:
            system_message = 'You are a useful assistant specialized in tourism for Ecuador and you answer in Spanish, you must be as clear and precise in your answers if a lot of rounding is direct.'

        combined_prompt = f"""
       {prompt}
        1. Provide a detailed and accurate description of the place.
        2. Describe the typical food of the region mentioned in the prompt.
        3. List the languages spoken in the region described.
        4. Describe the traditional music associated with the place.
        5. Describe the regions associated with the place.
        """

        response = openai.chat.completions.create(
            model='gpt-4',
            messages=[
                {'role': 'system', 'content': system_message},
                {'role': 'user', 'content': combined_prompt}
            ],
            temperature=0.9,
            max_tokens=500
        )
        print('XD', response)

        content = response.choices[0].message.content

        parts = content.split('\n\n')
        if len(parts) < 5:
            return Response({'message': content}, status=200)


        description_place = parts[0]
        typical_food = parts[1]
        languages = parts[2]
        traditional_music = parts[3]
        regions = parts[4]

        """ generate_image = generate_image_ia(prompt) """
        map_url = get_google_maps_static_image(prompt)


        response_data = {
            'description_place': description_place,
            'typical_food': typical_food,
            'languages': languages,
            'traditional_music': traditional_music,
            'city_tourist_map': '',  # Se puede usar Google Maps Static API o similar aquí
            'map_of_tourist_places_in_ecuador': '',  # Similar al campo anterior
            'hotels': '',  # Podrías integrar una API de hoteles aquí
            'regions': regions,
            'location': map_url,
        }
        """ 'image': generate_image, """
        print('DATA RESPONSE: ', response_data)
        return Response(response_data)

    except Exception as e:
        return Response({'error': str(e)}, status=400)

def generate_image_ia(prompt):
    response = openai.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size="512x512",
        quality="standard",
        n=1,
    )
    print(response)
    return response.data[0].url


import requests

def get_google_maps_static_image(location: str) -> str:
    google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    google_maps_static_url = 'https://maps.googleapis.com/maps/api/staticmap'

    params = {
        'center': location,
        'zoom': 9,
        'size': '800x600',
        'maptype': 'roadmap',
        'markers': f'color:red|{location}',
        'key': google_maps_api_key,
    }

    response = requests.get(google_maps_static_url, params=params)

    if response.status_code == 200:
        return response.url
    else:
        return ''

#CRUD BY PLACE-TOURISM

@api_view(['GET'])
def getAll(request):
    if request.method == 'GET':
        placeTourism = TouristPlace.objects.all()
        serializer = TouristPlaceListSerializer(placeTourism, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getById(request, id):
    placeTourism = get_object_or_404(TouristPlace, pk=id)
    serializer = TouristPlaceReadSerializer(placeTourism)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = TouristPlaceDetailWriteSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        print('validated data:', serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print('validation errors:', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, id):
    placeTourism = get_object_or_404(TouristPlace, pk=id)
    serializer = TouristPlaceDetailWriteSerializer(placeTourism, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def patch (request, id):
    placeTourism = get_object_or_404(placeTourism, pk=id)
    serializer = TouristPlaceDetailWriteSerializer(placeTourism, data = request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteById(request, id):
    placeTourism = get_object_or_404(TouristPlace, pk=id)
    if placeTourism.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    placeTourism.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def deleteUsersById(request, id):
    try:
        place = TouristPlace.objects.get(pk=id)
    except TouristPlace.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    users_data = request.data.get('users', [])
    if not isinstance(users_data, list):
        return Response({'error': 'Users must be a list of user IDs.'}, status=status.HTTP_400_BAD_REQUEST)

    users_to_remove = CustomUser.objects.filter(id__in=users_data)
    place.users.remove(*users_to_remove)

    return Response({'message': 'Users removed successfully.'}, status=status.HTTP_200_OK)