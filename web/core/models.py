
from django.db import models

# Create your models here.

#MODELO PARA CATEGORIAS

class Categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True,verbose_name="Id Categoria")
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre Categoria")
        
    def __str__(self):
        return self.nombreCategoria
        
#MODELO PARA USUARIOS

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True,verbose_name="Id Usuario")
    nombreusuario = models.CharField(max_length=100,verbose_name="Nombre Usuario")
    correousuario = models.CharField(max_length=200,verbose_name="Correo Usuario")
    contrasenausuario = models.CharField(max_length=50,verbose_name="Contraseña Usuario")
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreusuario
    