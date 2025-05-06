from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usuarios.views import login_view, register_view, dashboard_view, logout_view, beneficiario_view
from usuarios.views.beneficiario_view import lista_beneficiarios, añadir_beneficiario, eliminar_beneficiario, \
    editar_beneficiario
from usuarios.views.cuenta_view import detalle_cuenta, ingresar_dinero, retirar_dinero, realizar_transferencia, \
    crear_cuenta
from usuarios.views.movimientos_view import lista_movimientos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/usuarios/', include('usuarios.urls')),

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),

    path('cuenta/<int:cuenta_id>/', detalle_cuenta, name='detalle_cuenta'),
    path('cuenta/<int:cuenta_id>/ingresar/', ingresar_dinero, name='ingresar_dinero'),
    path('cuenta/<int:cuenta_id>/retirar/', retirar_dinero, name='retirar_dinero'),
    path('cuenta/<int:cuenta_id>/transferir/', realizar_transferencia, name='realizar_transferencia'),
    path('cuentas/nueva/', crear_cuenta, name='crear_cuenta'),


    path('beneficiarios/', lista_beneficiarios, name='lista_beneficiarios'),
    path('beneficiarios/añadir/', añadir_beneficiario, name='añadir_beneficiario'),
    path('beneficiarios/editar/<int:beneficiario_id>/', editar_beneficiario, name='editar_beneficiario'),
    path('beneficiarios/eliminar/<int:beneficiario_id>/', eliminar_beneficiario, name='eliminar_beneficiario'),

path('movimientos/', lista_movimientos, name='lista_movimientos'),
]
