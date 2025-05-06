from django.contrib.auth.models import User
from django.db import models

class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    carnet = models.IntegerField()
