from rest_framework import viewsets
from ..models.experiencia import Experiencia
from ..serializer.experiencia import ExperienciaSerializer

class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer