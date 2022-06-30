from asyncore import read
from .models import Producto,tipo
from rest_framework import serializers

class tipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    tipo_nombre = serializers.CharField(read_only=True,source="tipo.nombre")
    tipo_id = serializers.PrimaryKeyRelatedField(queryset=tipo.objects.all(), source="tipo")
    tipo = tipoSerializer(read_only=True)
    class Meta:
        model = Producto
        fields = '__all__'