from . import models
from rest_framework import serializers


class CategoriaSerializer(serializers.ModelSerializer):
    n_tareas = serializers.ReadOnlyField(source='tareas')

    class Meta:
        model = models.Categoria
        fields = (
            'id',
            'nombre',
            'n_tareas',
            'color'
        )


class TareaSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    categoria_color = serializers.ReadOnlyField(source='categoria.color')
    creacion = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = models.Tarea
        fields = (
            'id',
            'usuario',
            'descripcion',
            'completada',
            'creacion',
            'actualizacion',
            'categoria',
            'categoria_nombre',
            'categoria_color'
        )

    def create(self, validate_data):
        if not self.context['request'].user.is_anonymous:
            validate_data['usuario'] = self.context['request'].user
            return super().create(validate_data)
        raise serializers.ValidationError({'error': 'El usuario debe estar autenticado'})


