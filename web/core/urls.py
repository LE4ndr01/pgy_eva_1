from django.urls import path
from .views import inicio, nosotros, contacto,\
                    venta, seguimiento, dashuser, ordenes, formulario, crear,registro


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
]
