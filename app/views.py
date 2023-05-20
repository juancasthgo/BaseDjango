from django.shortcuts import get_object_or_404, render, redirect
from .models import Producto
from .forms import ContactoForm, ProductoForm

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html',data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Enviado!"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado!"
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)


def listar_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/producto/listar.html',data)


def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        data["form"] = formulario   

    return render(request, 'app/producto/modificar.html', data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar")