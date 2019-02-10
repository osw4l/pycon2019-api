from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=50,
        unique=True
    )
    color = models.CharField(
        max_length=30,
        default='cyan darken-1'
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

    def tareas(self):
        return Tarea.objects.filter(categoria=self).count()


class Tarea(models.Model):
    usuario = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='data'
    )
    descripcion = models.TextField()
    completada = models.BooleanField(
        default=False
    )
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def set_state(self):
        self.completada = not self.completada
        self.save()

