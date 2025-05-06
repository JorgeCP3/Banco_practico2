from rest_framework import serializers

from usuarios.models import Persona


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombre', 'apellido', 'carnet', 'username', 'password']
