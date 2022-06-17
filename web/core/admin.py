from django.contrib import admin
from .models import tipo,Producto,Contactos

# Register your models here.
# Administrar modelo

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","nuevo","tipo"]
    list_editable = ["precio"]
    search_fields =["nombre"]
    list_filter = ["tipo","nuevo"]
    list_per_page = 10
    
class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre","email","tipo_consulta","aviso","mensajes","fecha_enviado"]
    search_fields =["nombre","email"]
    list_filter = ["tipo_consulta","aviso"]
    list_per_page = 5  


admin.site.register(tipo)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Contactos,ContactoAdmin)

