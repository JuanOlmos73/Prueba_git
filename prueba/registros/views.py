from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404, redirect


def consultariosComentarioContacto(request):
    comentarios = ComentarioContacto.objects.all()

    return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})




def principal(request):
    alumnos=Alumnos.objects.all()

    return render(request,"registros/principal1.html",{'alumnos':alumnos})






def eliminarComentarioContacto(request, id,
    confirmacion = 'registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method== 'POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaContacto.html",
              {'comentarios':comentarios})
    
    return render(request, confirmacion, {'object':comentario})


def consultarComentarioIndiviual(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request,'registros/formEditarComentario.html',{'comentario':comentario})

def editarComentarioContacto(request,id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
            form.save()
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})

    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})         






def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
                form.save()
                comentarios = ComentarioContacto.objects.all()
                return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
    form = ComentarioContactoForm()

    return render(request, 'registros/contacto.html',{'form':form})


def contacto(request):
    return render(request,"registros/contacto.html")