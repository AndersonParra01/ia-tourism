from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'names', 'lastnames']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'names': {'required': False},
            'lastnames': {'required': False},
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        names = validated_data.get('names')
        
        if not username:
            raise serializers.ValidationError({"username": "This field is required."})
        if not password:
            raise serializers.ValidationError({"password": "This field is required."})
        if not names:
            raise serializers.ValidationError({"names": "This field is required."})

        lastnames = validated_data.get('lastnames', '')

        user = CustomUser(
            username=username,
            names=names,
            lastnames=lastnames
        )
        user.set_password(password)
        user.save()
        return user


class UserSerializerDetail(serializers.ModelSerializer):
    places = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'names', 'lastnames', 'places']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'names': {'required': False},
            'lastnames': {'required': False},
        }

    def get_places(self, obj):
        from tourism.serializers import TouristPlaceListSerializer
        serializer = TouristPlaceListSerializer(obj.places.all(), many=True)
        return serializer.data

    def validate(self, data):
        if self.instance is None and not data.get('password'):
            raise serializers.ValidationError({"password": "Password is required during creation."})
        return data

    def create(self, validated_data):
        places_data = validated_data.pop('places', [])
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            names=validated_data.get('names', ''),
            lastnames=validated_data.get('lastnames', '')
        )
        if places_data:
            user.places.set(places_data)
            
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.names = validated_data.get('names', instance.names)
        instance.lastnames = validated_data.get('lastnames', instance.lastnames)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()

        places_data = validated_data.get('places', None)
        if places_data is not None:
            instance.places.set(places_data)

        return instance