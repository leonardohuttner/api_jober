from rest_framework import viewsets,generics
from ..models.candidato_processo import CandidatoProcesso
from ..serializer.candidato_processo import CandidatoProcessoSerializer, ListaProcessoUsuarioSerializer, ListaUsuarioEmProcessosSerializer

class CandidatoProcessoViewSet(viewsets.ModelViewSet):
    queryset = CandidatoProcesso.objects.all()
    serializer_class = CandidatoProcessoSerializer

class ListaProcessoUsuario(generics.ListAPIView):
    """Listando processos onde o usuario se inscreveu"""
    def get_queryset(self):
        queryset = CandidatoProcesso.objects.filter(perfil_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaProcessoUsuarioSerializer

class ListaUsuariosProcesso(generics.ListAPIView):
    def get_queryset(self):
        queryset = CandidatoProcesso.objects.filter(processo_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaUsuarioEmProcessosSerializer