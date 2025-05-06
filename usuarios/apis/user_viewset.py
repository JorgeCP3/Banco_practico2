from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nombre', 'apellido')


class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class AuthViewSet(viewsets.ViewSet):

    @action(methods=['post'], detail=False, url_path='register')
    def register(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not password or not username:
            return Response({'error': 'El usuario y la contraseña son requeridos'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'El usuario ya está en uso'}, status=400)
        user = User.objects.create_user(username, username, password)
        return Response({'id': user.id, 'username': user.username}, status=201)
