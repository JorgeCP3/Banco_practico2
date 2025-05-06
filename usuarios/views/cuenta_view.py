from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from usuarios.models import Cuenta, Beneficiario, Movimiento

def detalle_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    beneficiarios = Beneficiario.objects.filter(persona=request.user.persona)

    return render(request, 'usuarios/detalle_cuenta.html', {
        'cuenta': cuenta,
        'beneficiarios': beneficiarios,
    })

def realizar_transferencia(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)

    if request.method == 'POST':
        monto = float(request.POST['monto'])
        nroCuentaBeneficiario = request.POST['beneficiario']

        if monto > cuenta.saldo:
            messages.error(request, 'Saldo insuficiente para realizar la transferencia.')
            return redirect('detalle_cuenta', cuenta_id=cuenta.id)

        try:
            beneficiario = Beneficiario.objects.get(nroCuenta=nroCuentaBeneficiario)
            cuenta_beneficiario = get_object_or_404(Cuenta, nro_cuenta=nroCuentaBeneficiario)
        except Beneficiario.DoesNotExist:
            messages.error(request, 'El beneficiario no existe.')
            return redirect('detalle_cuenta', cuenta_id=cuenta.id)

        cuenta.saldo -= monto
        cuenta.save()
        cuenta_beneficiario.saldo += monto
        cuenta_beneficiario.save()

        Movimiento.objects.create(
            tipo='egreso',
            cantidad=monto,
            cuenta=cuenta
        )

        Movimiento.objects.create(
            tipo='ingreso',
            cantidad=monto,
            cuenta=cuenta_beneficiario
        )

        messages.success(request,
                         f'Transferencia de ${monto:.2f} realizada con éxito a la cuenta N° {nroCuentaBeneficiario}.')

    return redirect('detalle_cuenta', cuenta_id=cuenta.id)

def ingresar_dinero(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    if request.method == 'POST':
        monto = float(request.POST['monto'])
        cuenta.saldo += monto
        cuenta.save()

        Movimiento.objects.create(
            tipo='ingreso',
            cantidad=monto,
            cuenta=cuenta
        )

        messages.success(request, f'Se ingresaron ${monto:.2f} correctamente.')
    return redirect('detalle_cuenta', cuenta_id=cuenta.id)

def retirar_dinero(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    if request.method == 'POST':
        monto = float(request.POST['monto'])
        if monto > cuenta.saldo:
            messages.error(request, 'Saldo insuficiente para retirar esa cantidad.')
        else:
            cuenta.saldo -= monto
            cuenta.save()

            Movimiento.objects.create(
                tipo='egreso',
                cantidad=monto,
                cuenta=cuenta
            )

            messages.success(request, f'Se retiraron ${monto:.2f} correctamente.')
    return redirect('detalle_cuenta', cuenta_id=cuenta.id)

def crear_cuenta(request):
    if request.method == 'POST':
        saldo = float(request.POST['saldo'])
        cuenta = Cuenta.objects.create(saldo=saldo, persona=request.user.persona)
        messages.success(request, f'Cuenta creada con éxito. N° {cuenta.nro_cuenta}')
        return redirect('detalle_cuenta', cuenta_id=cuenta.id)
    return redirect('dashboard')  # o donde prefieras
