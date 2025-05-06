from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Persona

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class PersonaSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Persona
        fields = ['id', 'nombre', 'apellido', 'carnet', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        persona = Persona.objects.create(user=user, **validated_data)
        return persona
