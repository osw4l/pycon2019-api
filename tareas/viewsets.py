from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models
from . import serializers


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def tareas(self, request, pk=None):
        tareas = models.Tarea.objects.filter(
            usuario=self.request.user,
            categoria_id=pk
        )
        serializer = serializers.TareaSerializer(tareas, many=True)
        return Response(serializer.data)


class TareaViewSet(viewsets.ModelViewSet):
    queryset = models.Tarea.objects.all()
    serializer_class = serializers.TareaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return models.Tarea.objects.filter(
            usuario=self.request.user
        )

    @action(detail=False)
    def completadas(self, request):
        tareas = self.get_queryset().filter(completada=True)
        serializer = self.serializer_class(tareas, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def no_completadas(self, request):
        tareas = self.get_queryset().filter(completada=False)
        serializer = self.serializer_class(tareas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def cambiar_estado(self, request, pk=None):
        tarea = models.Tarea.objects.get(id=pk)
        tarea.set_state()
        serializer = self.serializer_class(tarea)
        return Response(serializer.data)

