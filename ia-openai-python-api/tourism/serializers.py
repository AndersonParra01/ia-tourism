from rest_framework import serializers
from .models import TouristPlace
from user.models import CustomUser
from user.serializers import UserSerializer

class TouristPlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristPlace
        fields = ['id', 'name', 'description', 'location']


from rest_framework import serializers
from .models import TouristPlace
from user.models import CustomUser

class TouristPlaceDetailWriteSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())

    class Meta:
        model = TouristPlace
        fields = ['id', 'name', 'description', 'image', 'location', 'users']

    def create(self, validated_data):
        # Extraemos los usuarios del validated_data
        users_data = validated_data.pop('users', [])
        # Creamos el lugar turístico con los datos restantes
        place = TouristPlace.objects.create(**validated_data)
        # Asignamos los usuarios al lugar
        place.users.set(users_data)
        return place
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.location = validated_data.get('location', instance.location)
        instance.save()

        if 'users' in validated_data:
            new_users = validated_data.get('users', [])

            if new_users:
            # Obtener los IDs de los usuarios ya existentes
                existing_user_ids = set(instance.users.values_list('id', flat=True))
            
                for user_id in new_users:
                    if user_id not in existing_user_ids:
                    # Agregar el usuario si no está en la lista existente
                        instance.users.add(user_id)
                    else:
                    # Si el usuario ya está en la lista, no hacer nada
                        continue
            else:
            # No hacer nada si la lista de usuarios es vacía
                return instance

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
        fields = ['id', 'name', 'description', 'image', 'location', 'users']