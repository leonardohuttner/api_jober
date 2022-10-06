from rest_framework import viewsets
from ..models.projeto import Projeto
from ..serializer.projeto import ProjetoSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer