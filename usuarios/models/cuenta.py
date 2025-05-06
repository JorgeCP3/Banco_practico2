import random

from django.db import models

from usuarios.models import Persona

def generate_random_number():
    return random.randint(100000, 999999)

class Cuenta(models.Model):
    nro_cuenta = models.IntegerField(default=generate_random_number, editable=False, unique=True)
    saldo = models.FloatField()

    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='cuentas')
