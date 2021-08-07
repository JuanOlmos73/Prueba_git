"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name, stat
from django.contrib import admin
from django.urls import path
from inicio import views as p
from django.conf import settings
from registros import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="principal1"),
    path('contacto/',views.contacto, name="Contacto"),
    path('formulario/',p.formulario, name="formulario"),
    path('ejemplo/',p.ejemplo, name="Ejemplo"),
    path('registrar/',views.registrar,name="Registrar"),
    path('consultarComentario/',views.consultariosComentarioContacto,name="Comentarios"),   
    path('eliminarComentario/<int:id>/',views.eliminarComentarioContacto,name="Eliminar"),  
    path('formEditarComentario/<int:id>/',views.consultarComentarioIndiviual,name="ConsultaIndividual"),
    path('editarComentario/<int:id>/',views.editarComentarioContacto,name="Editar"),  
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

