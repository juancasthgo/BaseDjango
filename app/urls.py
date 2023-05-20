from django.urls import path
from .views import agregar_producto, contacto, eliminar_mensaje, eliminar_producto, galeria, home, listacontacto, listar_productos, modificar_producto, registro

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar/', agregar_producto, name="agregar"),
    path('listar/', listar_productos, name="listar"),
    path('modificar/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro', registro, name="registro"),
    path('mensajes/', listacontacto,  name="listacontacto"),
    path('eliminarmensaje/<id>/', eliminar_mensaje, name="eliminar_mensaje"),







]
