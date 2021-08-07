from django.contrib import admin 
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto
# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula','nombre','carrera','turno')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')
admin.site.register(Alumnos,AdministrarModelo)

class AdministrarComentario(admin.ModelAdmin):
    readonly_fields=('created','id')
    list_display = ('id','comment')
    search_fields =('id','created')
    date_hierarchy = 'created'
    list_filter = ('created', 'id')
admin.site.register(Comentario, AdministrarComentario)



class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id','mensaje')
    readonly_fields=('created','id')
    search_fields =('id','created')
    date_hierarchy = 'created'


admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

