from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from usuarios.models import Persona


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')

    return render(request, 'usuarios/registration/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        carnet = request.POST['carnet']

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            persona = Persona.objects.create(
                nombre=nombre,
                apellido=apellido,
                carnet=carnet,
                user=user  #
            )

            messages.success(request, 'Registro exitoso, ahora puedes iniciar sesión')
            return redirect('login')

        except Exception as e:
            messages.error(request, 'Hubo un error al crear el usuario, intenta nuevamente')

    return render(request, 'usuarios/registration/register.html')
