from rest_framework import viewsets
from ..models.educacao import Educacao
from ..serializer.educacao import EducacaoSerializer

class EducacaoViewSet(viewsets.ModelViewSet):
    queryset = Educacao.objects.all()
    serializer_class = EducacaoSerializer