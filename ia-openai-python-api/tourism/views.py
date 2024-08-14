from django.shortcuts import get_object_or_404, render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import openai
from deep_translator import GoogleTranslator
from rest_framework import viewsets
from .models import TouristPlace
from .serializers import TouristPlaceDetailSerializer, TouristPlaceListSerializer
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

""" @api_view(['GET'])
def get_tourist_recommendations(request):
    print('REQUE', request)
    prompt = request.query_params.get('prompt')
    language = request.query_params.get('language', 'en')
    print('LANG', language)
    if not prompt:
        return Response({'error': 'prompt query parameter is required'}, status=400)

    try:
        selected_language = language_selector(language)
    except ValueError as e:
        return Response({'error': str(e)}, status=400)
    
    openai.api_key = settings.OPENAI_API_KEY

    try:
        response = openai.chat.completations.create(
            model='gpt-4',
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant specialized in tourism for Ecuador.'},
                {'role': 'user', 'content': prompt}
            ],
            temperature=0.8,
            max_tokens=1000
        )
        recommendations = response.choices[0].message.content
        print('RECO', recommendations)
        translator = GoogleTranslator(source='auto', target=selected_language)
        translated_recommendations = translator.translate(recommendations)
        
        return Response({'response': translated_recommendations})

    except Exception as e:
        return Response({'error': str(e)}, status=500)
 """

@api_view(['GET'])
def get_completion(request):
    prompt = request.query_params.get('prompt')
    openai.api_key = settings.OPENAI_API_KEY

    try:
        # Generar la respuesta principal usando la nueva API de OpenAI
        response = openai.chat.completions.create(
            model='gpt-4',
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant specialized in tourism for Ecuador.'},
                {'role': 'user', 'content': prompt}
            ],
            temperature=0.8,
            max_tokens=1000
        )
        
        # Extraer el contenido del mensaje desde la respuesta
        print('CONTENT', response.choices[0].message.content)
        content = response.choices[0].message.content

        # Usar OpenAI para generar las respuestas detalladas
        description_place = generate_description(prompt)
        typical_food = generate_typical_food(prompt)
        languages = generate_languages_info(prompt)
        traditional_music = generate_traditional_music(prompt)
        regions = generate_regions_info(prompt)

        # Formar el JSON de respuesta
        response_data = {
            'description_place': description_place,
            'image': '',  # Esto se puede llenar más adelante con una API de imágenes
            'location': '',  # Esto también puede ser llenado con una API de localización
            'typical_food': typical_food,
            'languages': languages,
            'traditional_music': traditional_music,
            'city_tourist_map': '',  # Se puede usar una API de mapas para esto
            'map_of_tourist_places_in_ecuador': '',  # Similar al campo anterior
            'hotels': '',  # Podrías integrar una API de hoteles aquí
            'regions': regions,
        }

        return Response(response_data)

    except Exception as e:
        return Response({'error': str(e)}, status=400)


def generate_description(prompt):
    response = openai.chat.completions.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'Provide a detailed and accurate description of the place based on the given prompt.'},
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    return response.choices[0].message.content


def generate_typical_food(prompt):
    response = openai.chat.completions.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'Describe the typical food of the region mentioned in the prompt.'},
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content


def generate_languages_info(prompt):
    response = openai.chat.completions.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'List the languages spoken in the region described in the prompt.'},
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].message.content


def generate_traditional_music(prompt):
    response = openai.chat.completions.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'Describe the traditional music associated with the place mentioned in the prompt.'},
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content


def generate_regions_info(prompt):
    response = openai.chat.completions.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'Describe the regions associated with the place mentioned in the prompt.'},
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return response.choices[0].message.content

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
    serializer = TouristPlaceDetailSerializer(placeTourism)
    return Response(serializer.data)

@api_view(['POST'])
def create (request):
    serializer = TouristPlaceDetailSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, id):
    placeTourism = get_object_or_404(TouristPlace, pk=id)
    serializer = TouristPlaceDetailSerializer(placeTourism, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def patch (request, id):
    placeTourism = get_object_or_404(placeTourism, pk=id)
    serializer = TouristPlaceDetailSerializer(placeTourism, data = request.data, partial=True)
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