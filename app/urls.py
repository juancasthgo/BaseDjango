from django.urls import path
from .views import agregar_producto, contacto, galeria, home, listar_productos

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar/', agregar_producto, name="agregar"),
    path('listar/', listar_productos, name="listar"),

]
