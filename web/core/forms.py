
from ast import Name
from tabnanny import verbose
from wsgiref.handlers import format_date_time
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contactos,Producto,tipo
from django.forms import ValidationError


class CustomUserCreationForm(UserCreationForm):
   def clean_nombre(self):
      nombre = self.cleaned_data['nombre']
      existe = User.objects.filter(nombre__iexact=nombre).exists()
      
      if existe:
         raise ValidationError("Nombre ya existe")
   class Meta:
      model = User
      fields =['username',"first_name","last_name", "email", "password1","password2"]
      
class ContactForm(forms.ModelForm):
   
   aviso = forms.BooleanField(required=True)
   class Meta:
         model = Contactos
         fields = '__all__'
         
class productoform(forms.ModelForm):
   fecha_ingresado= forms.DateField(widget=forms.SelectDateWidget())
   class Meta:
        model = Producto
        fields = '__all__'
        


class tipoform(forms.ModelForm):
   class Meta:
      model = tipo
      fields = '__all__'