from django.shortcuts import render
from usuarios.models import Movimiento, Cuenta, Persona


def lista_movimientos(request):
    persona = Persona.objects.get(user=request.user)

    cuentas = persona.cuentas.all()

    movimientos = Movimiento.objects.filter(cuenta__in=cuentas).order_by('-fecha')

    context = {
        'movimientos': movimientos,
    }
    return render(request, 'usuarios/lista_movimientos.html', context)
