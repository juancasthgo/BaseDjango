from django.urls import path
from .views import agregar_producto, contacto, eliminar_producto, galeria, home, listar_productos, modificar_producto

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar/', agregar_producto, name="agregar"),
    path('listar/', listar_productos, name="listar"),
    path('modificar/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar/<id>/', eliminar_producto, name="eliminar_producto"),



]
