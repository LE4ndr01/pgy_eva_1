from django.urls import path
from .views import inicio, nosotros, contacto,\
                    venta, seguimiento, dashuser, ordenes, formulario,\
                    crear,registro,compra,agregar_producto,eliminar_producto,\
                    listar_producto,actualizar_producto


urlpatterns = [
    path('', inicio, name= "inicio"),
    path('nosotros', nosotros, name= "nosotros"),
    path('contacto', contacto, name= "contacto"),
    path('venta', venta, name= "venta"),
    path('seguimiento', seguimiento, name= "seguimiento"),
    path('dashuser', dashuser, name= "dashuser"),
    path('ordenes', ordenes, name= "ordenes"),
    path('formulario', formulario, name= "formulario"),
    path('crear', crear, name= "crear"),
    path('registro/', registro, name= "registro"),
    path('compra', compra, name= "compra"),
    path('agregar-producto/', agregar_producto, name= "agregar_producto"),
    path('eliminar_producto', eliminar_producto, name= "eliminar_producto"),
    path('listar_producto', listar_producto, name= "listar_producto"),
    path('actualizar_producto', actualizar_producto, name= "actualizar_producto"),
]
