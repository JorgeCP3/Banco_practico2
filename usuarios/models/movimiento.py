from django.db import models

class Movimiento(models.Model):
    tipo_movimiento = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]

    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=tipo_movimiento)

    cuenta = models.ForeignKey('Cuenta', on_delete=models.CASCADE)

