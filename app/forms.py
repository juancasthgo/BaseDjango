from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# FORMULARIO CONTACTO
class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=15) #VALIDACION 1
    class Meta:
        model = Contacto
        fields = '__all__'

# FORMULARIO AGREGAR PRODUCTO
class ProductoForm(forms.ModelForm):
    imagen = forms.ImageField(required=False) #VALIDACION 1
    nombre = forms.CharField(min_length=3, max_length=30) #VALIDACION 2
    descripcion = forms.CharField(required=False) #VALIDACION 3
    class Meta:
        model = Producto
        fields = '__all__'

# FORMULARIO REGISTRO
class CustomUserCreation(UserCreationForm):
    email = forms.CharField(required=True) #VALIDACION 1
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']