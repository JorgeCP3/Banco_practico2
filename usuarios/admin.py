from django.contrib import admin

from usuarios.models import Persona
from usuarios.models import Beneficiario
from usuarios.models import Cuenta
from usuarios.models import Movimiento

# Register your models here.
admin.site.register(Persona)
admin.site.register(Cuenta)
admin.site.register(Movimiento)
admin.site.register(Beneficiario)
