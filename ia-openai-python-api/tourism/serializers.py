from rest_framework import serializers
from .models import TouristPlace
from user.models import CustomUser
from user.serializers import UserSerializer

class TouristPlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristPlace
        fields = ['id', 'description_place', 'typical_food', 'languages', 'traditional_music', 'city_tourist_map', 'map_of_tourist_places_in_ecuador', 'hotels', 'regions', 'location', 'especific_destination', 'created_at']

class TouristPlaceDetailWriteSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())

    class Meta:
        model = TouristPlace
        fields = ['id', 'description_place', 'typical_food', 'languages', 'traditional_music', 'city_tourist_map', 'map_of_tourist_places_in_ecuador', 'hotels', 'regions', 'especific_destination','location', 'created_at', 'users']

    def create(self, validated_data):
        print('validated_data:', validated_data)
        users_data = validated_data.pop('users', [])
        place = TouristPlace.objects.create(**validated_data)
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

class TouristPlaceReadSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = TouristPlace
        fields = ['id', 'description_place', 'typical_food', 'languages', 'traditional_music', 'city_tourist_map', 'map_of_tourist_places_in_ecuador', 'hotels', 'regions', 'especific_destination', 'location', 'created_at','users']
