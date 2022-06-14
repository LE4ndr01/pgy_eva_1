from django.shortcuts import render
from .models import Producto


# Create your views here.
def inicio (request):
    return render(request, 'core/index.html')
def nosotros (request):
    return render(request, 'core/nosotros.html')
def contacto (request):
    return render(request, 'core/forcontacto.html')
def venta (request):
    Productos = Producto.objects.all()
    data ={
        'productos':Productos
    }
    return render(request, 'core/ventasproductos.html', data)
def seguimiento (request):
    return render(request, 'core/seguimiento.html')
def dashuser (request):
    return render(request, 'core/dashuser.html')
def ordenes (request):
    return render(request, 'core/ordenes.html')
def formulario (request):
    return render(request, 'core/formulario.html')
def crear (request):
    return render(request, 'core/ccuenta.html')
