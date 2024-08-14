from rest_framework import serializers
from .models import TouristPlace
from user.models import CustomUser
from user.serializers import UserSerializer

class TouristPlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristPlace
        fields = ['id', 'name', 'description', 'location']

class TouristPlaceDetailSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = TouristPlace
        fields = ['id', 'name', 'description', 'image', 'location', 'users']

    def create(self, validated_data):
        users_data = validated_data.pop('users', [])
        place = TouristPlace.objects.create(**validated_data)
        if users_data:
            place.users.set(users_data)
        return place
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.location = validated_data.get('location', instance.location)
        instance.save()

        users_data = validated_data.get('users', None)
        if users_data is not None:
            current_users = set(instance.users.all())
            new_users = set(users_data)
            updated_users = current_users.union(new_users)
            instance.users.set(updated_users)

        return instance
