from django.db import models

from usuarios.models import Persona


class Beneficiario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nroCuenta = models.IntegerField()

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='beneficiarios')


