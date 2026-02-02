"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('api/cazadores/', GrupoCazadores.as_view(), name='cazadores'),
    path('api/cazadores/<int:pk>/', GrupoCazadoresDetail.as_view(), name='cazadores_detail'),
    path('api/roles/', GrupoRoles.as_view(), name='roles'),
    path('api/roles/<int:pk>/', GrupoRolesDetail.as_view(), name='roles_detail'),
    path('api/respiraciones/', GrupoRespiraciones.as_view(), name='respiraciones'),
    path('api/respiraciones/<int:pk>/', GrupoRespiracionesDetail.as_view(), name='respiraciones_detail'),
    path('api/posturas/', GrupoPosturas.as_view(), name='posturas'),
    path('api/posturas/<int:pk>/', GrupoPosturasDetail.as_view(), name='posturas_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
