from django.db import models

# Create your models here.

#MODELO PARA CATEGORIAS

class tipo(models.Model):
    
    nombre = models.CharField(max_length=50,verbose_name="Nombre Tipo")
    
        
    def __str__(self):
        return self.nombre
        
#MODELO PARA PRODUCTO

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion= models.TextField()
    seg_desc=models.TextField()
    nuevo = models.BooleanField()
    tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)
    fecha_ingresado = models.DateField()
    imagen = models.ImageField(upload_to="producto", null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
    
#MODELO PARA CONTACTO

opcion_consulta = [
    [0,"Consulta"],
    [1,"Sugerencia"],
    [2,"Reclamo"],
    [3,"No deseo Responder"],
    [4,"otro"],
    
    
]

class Contactos(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opcion_consulta)
    mensajes= models.TextField(max_length=500)
    aviso = models.BooleanField(verbose_name="Acepto Terminos y Condiciones")
    fecha_enviado= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.nombre
