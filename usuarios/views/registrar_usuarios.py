from rest_framework import generics

from usuarios.models import Persona
from usuarios.serializers import PersonaSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
