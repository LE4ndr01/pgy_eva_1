
from distutils.command.upload import upload
from django.db import models

# Create your models here.

#MODELO PARA CATEGORIAS

class tipo(models.Model):
    
    nombreTipo = models.CharField(max_length=50,verbose_name="Nombre Tipo")
        
    def __str__(self):
        return self.nombreTipo
        
#MODELO PARA PRODUCTO

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion= models.TextField()
    seg_desc=models.TextField()
    nuevo = models.BooleanField()
    tipo = models.ForeignKey(tipo, on_delete=models.PROTECT)
    fecha_ingresado = models.DateField()
    imagen = models.ImageField(upload_to="producto", null=True)
    def __str__(self):
        return self.nombre
    
#MODELO PARA CONTACTO

