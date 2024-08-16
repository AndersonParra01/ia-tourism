from rest_framework import serializers
from .models import TouristPlace
from user.models import CustomUser
from user.serializers import UserSerializer

class TouristPlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristPlace
        fields = ['id', 'typical_food', 'languages', 'traditional_music', 'city_tourist_map', 'map_of_tourist_places_in_ecuador', 'hotels', 'regions']

class TouristPlaceDetailWriteSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())

    class Meta:
        model = TouristPlace
        fields = ['id', 'typical_food', 'languages', 'traditional_music', 'city_tourist_map', 'map_of_tourist_places_in_ecuador', 'hotels', 'regions', 'users']

    def create(self, validated_data):
        # Extraemos los usuarios del validated_data
        users_data = validated_data.pop('users', [])
        # Creamos el lugar turístico con los datos restantes
        place = TouristPlace.objects.create(**validated_data)
        # Asignamos los usuarios al lugar
        place.users.set(users_data)
        return place
    
    def update(self, instance, validated_data):
        instance.typical_food = validated_data.get('typical_food', instance.typical_food)
        instance.languages = validated_data.get('languages', instance.languages)
        instance.traditional_music = validated_data.get('traditional_music', instance.traditional_music)
        instance.city_tourist_map = validated_data.get('city_tourist_map', instance.city_tourist_map)
        instance.map_of_tourist_places_in_ecuador = validated_data.get('map_of_tourist_places_in_ecuador', instance.map_of_tourist_places_in_ecuador)
        instance.hotels = validated_data.get('hotels', instance.hotels)
        instance.regions = validated_data.get('regions', instance.regions)
        instance.save()

        if 'users' in validated_data:
            instance.users.set(validated_data['users'])

        return instance
    class Meta:
        model = TouristPlace
        fields = ['id', 'name', 'description', 'image', 'location', 'users']

    def create(self, validated_data):
        # Extraemos la lista de usuarios de los datos validados
        users_data = validated_data.pop('users', [])
        # Creamos el lugar turístico con los datos restantes
        place = TouristPlace.objects.create(**validated_data)
        # Asignamos los usuarios al lugar turístico
        place.users.set(users_data)
        return place
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.location = validated_data.get('location', instance.location)
        instance.save()

        if 'users' in validated_data:
            instance.users.set(validated_data['users'])

        return instance

class TouristPlaceReadSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = TouristPlace
        fields = ['id', 'typical_food', 'languages', 'traditional_music', 'city_tourist_map', 'map_of_tourist_places_in_ecuador', 'hotels', 'regions', 'users']