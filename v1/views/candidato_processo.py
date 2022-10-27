from rest_framework import viewsets,generics
from v1.models.perfil import Perfil

from v1.serializer.perfil import PerfilSerializer
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
    """Buscar usuarios de um determinado processo"""
    def get_queryset(self):
        queryset = CandidatoProcesso.objects.filter(processo_id = self.request.query_params.get('id_processo'))
        return queryset
    serializer_class = ListaUsuarioEmProcessosSerializer