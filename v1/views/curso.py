from rest_framework import viewsets
from ..models.curso import Curso
from ..serializer.curso import CursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer