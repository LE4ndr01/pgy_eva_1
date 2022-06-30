from django.urls import path

from .views import inicio, nosotros, contacto,\
                    venta, seguimiento, dashuser, ordenes, formulario,\
                    crear,registro,compra,agregar_producto,eliminar_producto,\
                    listar_producto,actualizar_producto,Paginator,agregar_tipo,\
                    eliminar_tipo,actualizar_tipo,listar_tipo


urlpatterns = [
    path('', inicio, name= "inicio"),
    path('nosotros/', nosotros, name= "nosotros"),
    path('contacto/', contacto, name= "contacto"),
    path('venta/', venta, name= "venta"),
    path('seguimiento/', seguimiento, name= "seguimiento"),
    path('dashuser/', dashuser, name= "dashuser"),
    path('ordenes/', ordenes, name= "ordenes"),
    path('formulario/', formulario, name= "formulario"),
    path('crear/', crear, name= "crear"),
    path('registro/', registro, name= "registro"),
    path('compra/', compra, name= "compra"),
    path('agregar-producto/', agregar_producto, name= "agregar"),
    path('eliminar_producto/<id>/', eliminar_producto, name= "eliminar"),
    path('listar_producto/', listar_producto, name= "listar"),
    path('Modificar_producto/<id>/', actualizar_producto, name= "Modificar"),
    path('page/', Paginator, name= "page"),
    path('agregar-tipo/', agregar_tipo, name= "agregar_tipo"),
    path('eliminar_tipo/<id>/', eliminar_tipo, name= "eliminar_tipo"),
    path('listar_tipo/', listar_tipo, name= "listar_tipo"),
    path('Modificar_tipo/<id>/', actualizar_tipo, name= "Modificar_tipo"),
    
    
    
]
