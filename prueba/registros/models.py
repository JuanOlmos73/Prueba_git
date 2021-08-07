from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField

# Create your models here.
class Alumnos(models.Model):
    matricula = models.CharField(max_length=12,verbose_name="Mat")
    nombre = models.TextField()
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
class Comentario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    alumno=models.ForeignKey(Alumnos, on_delete=models.CASCADE,verbose_name="Alumno")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    comment =RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]

    def __str__(self):
        return self.comment

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario=models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contacttos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje