from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=30) #VALIDACION 1
    descripcion = forms.CharField(required=False) #VALIDACION 2

    class Meta:
        model = Producto
        fields = '__all__'
