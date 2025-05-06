from django.contrib.auth import logout
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from usuarios.models import Persona, Movimiento, Beneficiario

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    return Response({'message': f'Bienvenido {request.user.username}!'})
def dashboard_view(request):
    persona = Persona.objects.get(user=request.user)

    cuentas = persona.cuentas.all()
    movimientos = Movimiento.objects.filter(cuenta__in=cuentas)
    beneficiarios = Beneficiario.objects.filter(persona=persona)

    context = {
        'cuentas': cuentas,
        'movimientos': movimientos,
        'beneficiarios': beneficiarios,
    }
    return render(request, 'usuarios/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
