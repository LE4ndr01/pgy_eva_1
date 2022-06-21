
from django.shortcuts import redirect, render,get_object_or_404
from .models import Producto
from .forms import CustomUserCreationForm,ContactForm,productoform
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.http import Http404






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
    productos = Producto.objects.all()
    data ={
        'productos':productos
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

def eliminar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to='listar')

# metodo Actualizar

def actualizar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    
    data ={
       'form':productoform(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = productoform(data=request.POST,instance=producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar')
        data["form"] = formulario

    return render (request, 'crud/actualizar.html',data)

# metodo listar

def listar_producto(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    
    
    data={
        'entity':productos,
        'paginator':paginator
    }
    

    return render (request, 'crud/listar.html',data)
    
#------------------------------------------------

#Carrito de compras

