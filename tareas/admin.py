from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'color',
        'tareas'
    ]
    search_fields = [
        'nombre'
    ]


@admin.register(models.Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'categoria',
        'descripcion',
        'completada',
        'creacion',
        'actualizacion'
    ]
    search_fields = [
        'descripcion',
        'usuario__username',
        'categoria__nombre'
    ]
    list_filter = [
        'categoria',
        'usuario',
        'completada'
    ]



