from collections import UserString
from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.

def main(request):
    return render(request, 'index.html')

# =====================================CLASES DE API================================================
class GrupoCazadores(APIView):
    def get(self, request):
        data = Cazadores.objects.all()
        serializer = CazadoresSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GrupoCazadoresDetail(APIView):
    def get(self, request, pk=None):
        try:
            data = Cazadores.objects.get(id=pk)
            serializer = CazadoresSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Cazadores.DoesNotExist:
            return Response(data={'mensaje': 'No existe'}, status=status.HTTP_404_NOT_FOUND)

class GrupoRoles(APIView):
    def get(self, request):
        data = Rol.objects.all()
        serializer = RolesSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrupoRolesDetail(APIView):
    def get(self, request, pk=None):
        try:
            data = Rol.objects.get(id=pk)
            serializer = RolesSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Rol.DoesNotExist:
            return Response(data={'mensaje': "No existe ese Rol"}, status=status.HTTP_404_NOT_FOUND)

class GrupoRespiraciones(APIView):
    def get(self, request):
        data = Respiracion.objects.all()
        serializer = RespiracionesSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrupoRespiracionesDetail(APIView):
    def get(self, request, pk=None):
        try:
            data = Respiracion.objects.get(id=pk)
            serializer = RespiracionesSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Respiracion.DoesNotExist:
            return Response(data={'mensaje': "No existe esa respiracion"}, status=status.HTTP_404_NOT_FOUND)

class GrupoPosturas(APIView):
    def get(self, request):
        data = Postura.objects.all()
        serializer = PosturasSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrupoPosturasDetail(APIView):
    def get(self, request, pk=None):
        try:
            data = Postura.objects.get(id=pk)
            serializer = PosturasSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Postura.DoesNotExist:
            return Response(data={'mensaje': "No existe esa postura"}, status=status.HTTP_404_NOT_FOUND)