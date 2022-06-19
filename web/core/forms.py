
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contactos,Producto

class CustomUserCreationForm(UserCreationForm):
   class Meta:
      model = User
      fields =['username',"first_name","last_name", "email", "password1","password2"]
      
class ContactForm(forms.ModelForm):
       class Meta:
         model = Contactos
         fields = '__all__'
         
class productoform(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
        widgets = {
           "fecha_fabricacion": forms.SelectDateWidget()
         }