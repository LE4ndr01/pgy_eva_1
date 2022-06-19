
from django.shortcuts import redirect, render
from .models import Producto
from .forms import CustomUserCreationForm,ContactForm,productoform
from django.contrib.auth import login, authenticate






# Create your views here.
def inicio (request):
    return render(request, 'core/index.html')
def nosotros (request):
    return render(request, 'core/nosotros.html')
def contacto (request):
    
    data={
        'form':ContactForm()
    }
    
    if request.method == 'POST': 
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario
    
    return render(request, 'core/forcontacto.html',data)
def venta (request):
    Productos = Producto.objects.all()
    data ={
        'productos':Productos
    }
    return render(request, 'core/ventasproductos.html',data)
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

def compra (request):
    return render(request, 'core/compra.html')

# CRUD


# metodo Agregar

def agregar_producto(request):
    
    data ={
       
       'form':productoform()
        
    }
    if request.method == 'POST':
        formulario = productoform(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto agregado"
        else:
            data["form"] = formulario   
        

    return render (request, 'crud/agregar.html',data)

# metodo Eliminar

def eliminar_producto(request):

    return render (request, 'crud/eliminar.html')

# metodo Actualizar

def actualizar_producto(request):

    return render (request, 'crud/actualizar.html')

# metodo listar

def listar_producto(request):
    Productos = Producto.objects.all()
    data={
        'productos':Productos
    }
    

    return render (request, 'crud/listar.html',data)
    
#------------------------------------------------

#Carrito de compras

