from django.contrib.auth.views import LoginView
from django.urls import path

from usuarios.views.obtener_usuarios import PersonaListAPIView
from usuarios.views.registrar_usuarios import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('list/', PersonaListAPIView.as_view(), name='persona-list'),
]
