from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import Beneficiario, Persona

@login_required
def lista_beneficiarios(request):
    persona = request.user.persona
    beneficiarios = Beneficiario.objects.filter(persona=persona)
    return render(request, 'usuarios/beneficiarios.html', {'beneficiarios': beneficiarios})

@login_required
def añadir_beneficiario(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        nroCuenta = request.POST.get('nroCuenta')
        persona = Persona.objects.get(user=request.user)

        beneficiario = Beneficiario(
            nombre=nombre,
            apellido=apellido,
            nroCuenta=nroCuenta,
            persona=persona
        )
        beneficiario.save()

        return redirect('lista_beneficiarios')

    return render(request, 'usuarios/beneficiarios.html')

@login_required
def editar_beneficiario(request, beneficiario_id):
    beneficiario = get_object_or_404(Beneficiario, id=beneficiario_id, persona=request.user.persona)

    if request.method == "POST":
        beneficiario.nombre = request.POST.get('nombre')
        beneficiario.apellido = request.POST.get('apellido')
        beneficiario.nroCuenta = request.POST.get('nroCuenta')
        beneficiario.save()

        return redirect('lista_beneficiarios')

    return render(request, 'usuarios/editar_beneficiario.html', {'beneficiario': beneficiario})

@login_required
def eliminar_beneficiario(request, beneficiario_id):
    beneficiario = get_object_or_404(Beneficiario, id=beneficiario_id, persona=request.user.persona)
    beneficiario.delete()
    return redirect('lista_beneficiarios')
