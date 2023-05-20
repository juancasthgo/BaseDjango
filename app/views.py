from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Contacto, Producto
from .forms import ContactoForm, CustomUserCreation, ProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

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
            messages.success(request, "Agregado")

        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)






@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productos, 1) #cantidad de productos a ver en el paginator
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
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
            messages.success(request, "Producto Modificado")
            return redirect(to="listar")
        data["form"] = formulario   

    return render(request, 'app/producto/modificar.html', data)








def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto Eliminado")
    return redirect(to="listar")

def eliminar_mensaje(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    messages.success(request, "Mensaje Eliminado")
    return redirect(to="listacontacto")





def registro(request):
    data = { 
        'form': CustomUserCreation()
    }

    if request.method == 'POST':
        formulario = CustomUserCreation(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registracion Exitosa, Bienvenido")
            return redirect(to="home")
        data["form"] = formulario 
    return render(request, 'registration/registro.html', data)





#  PAGINAS LISTAR CONTACTO #
@permission_required('app.view_producto')
def listacontacto(request):
    productos = Contacto.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404

    data = { 
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listacontacto.html', data)