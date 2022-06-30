
from django.shortcuts import redirect, render,get_object_or_404
from .models import Producto, tipo
from .forms import CustomUserCreationForm,ContactForm,productoform,tipoform
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required,permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')
        
        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        return productos


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
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404
    data ={
        'entity':productos,
        'paginator':paginator
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
@login_required
def compra (request):
    return render(request, 'core/compra.html')

# CRUD PRODUCTO
# metodo Agregar
@permission_required('core.add_producto')
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
@permission_required('core.delete_producto')
def eliminar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to='listar')
# metodo Actualizar
@permission_required('core.change_producto')
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
@permission_required('core.view_producto')
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

# CRUD CATEGORIA
@permission_required('core.add_tipo')
def agregar_tipo(request):
    
    data ={
       
       'form':tipoform()
        
    }
    if request.method == 'POST':
        formulario = tipoform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Categoria agregada"
        else:
            data["form"] = formulario   
 
        

    return render (request, 'crud_tipo/agregar.html', data)
@permission_required('core.delete_tipo')
def eliminar_tipo(request,id):
    tipos = get_object_or_404(tipo, id=id)
    tipos.delete()
    return redirect(to='listar_tipo')
@permission_required('core.change_tipo')
def actualizar_tipo(request, id):
    
    tipos = get_object_or_404(tipo, id=id)
    
    data ={
       'form':tipoform(instance=tipos)
    }
    
    if request.method == 'POST':
        formulario = tipoform(data=request.POST,instance=tipos,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_tipo')
        data["form"] = formulario

    return render (request, 'crud_tipo/actualizar.html',data)
@permission_required('core.view_tipo')
def listar_tipo(request):
    tipos = tipo.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(tipos, 5)
        tipos = paginator.page(page)
    except:
        raise Http404
    
    
    data={
        'entity':tipos,
        'paginator':paginator
    }
    

    return render (request, 'crud_tipo/listar.html',data)
