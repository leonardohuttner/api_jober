from rest_framework import viewsets
from ..models.processo_seletivo import ProcessoSeletivo
from ..serializer.processo_seletivo import ProcessoSeletivoSerializer

class ProcessoSeletivoViewSet(viewsets.ModelViewSet):
    queryset = ProcessoSeletivo.objects.all()
    serializer_class = ProcessoSeletivoSerializer