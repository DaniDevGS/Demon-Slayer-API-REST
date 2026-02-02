from rest_framework import serializers
from .models import *

class CazadoresSerializer(serializers.ModelSerializer):
    rol = serializers.ReadOnlyField(source='rol.nombre')
    respiracion = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre', source='respiraciones')
    imagen = serializers.ImageField(source='imagen_cazador', read_only=True)

    class Meta:
        model = Cazadores
        fields = ['id', 'nombre', 'descripcion', 'rol', 'imagen', 'respiracion']

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'descripcion']

class RespiracionesSerializer(serializers.ModelSerializer):
    creador_original = serializers.ReadOnlyField(source='creador_original.nombre')
    derivada = serializers.ReadOnlyField(source='derivada_de.nombre')
    class Meta:
        model = Respiracion
        fields = ['id', 'nombre', 'descripcion', 'imagen_representativa', 'creador_original', 'derivada', 'color_catana']

class PosturasSerializer(serializers.ModelSerializer):
    respiracion = serializers.ReadOnlyField(source='respiracion.nombre')
    creador_de_postura = serializers.ReadOnlyField(source='creador_de_postura.nombre')
    class Meta:
        model = Postura
        fields = ['id', 'nombre', 'descripcion', 'numero', 'respiracion', 'imagen_accion', 'creador_de_postura']
