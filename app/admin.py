from django.contrib import admin
from .models import Contacto, Marca, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","marca"]
    list_editable = ["precio"]
    search_fields = ["nombre","marca"]
    list_filter = ["marca"]
    list_per_page =  10

# MODELO VISUALIZAR CONTACTO.
class ContactoProductoEdit(admin.ModelAdmin):
    list_display = ["nombre","correo","mensaje"]
    list_editable = ["mensaje"]
    search_fields = ["correo","nombre"]
    list_per_page =  10
    
admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto, ContactoProductoEdit)
