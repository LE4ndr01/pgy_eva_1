from django.contrib import admin
from .models import tipo,Producto

# Register your models here.
# Administrar modelo

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","nuevo","tipo"]
    list_editable = ["precio"]
    search_fields =["nombre"]
    list_filter = ["tipo","nuevo"]
    list_per_page = 10


admin.site.register(tipo)
admin.site.register(Producto,ProductoAdmin)