from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Producto
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate



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
    data ={
        'form':CustomUserCreationForm()
    }  
    if request.method == 'POST': 
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
        data["form"] = formulario
    return render(request, 'core/ccuenta.html')
def registro (request):
    
    data ={
        'form':CustomUserCreationForm()
    }  
    if request.method == 'POST': 
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
        data["form"] = formulario
        
    return render(request, 'registration/registrar.html',data)



