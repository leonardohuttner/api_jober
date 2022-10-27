from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from v1.models.perfil import Perfil
import json

from v1.models.processo_seletivo import ProcessoSeletivo

from v1.serializer.processo_seletivo import ProcessoSeletivoSerializer

from ..models.candidato_processo import  CandidatoProcesso

class CandidatoProcessoSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CandidatoProcesso
        fields = '__all__'

class ListaProcessoUsuarioSerializer(FlexFieldsModelSerializer):
    processo = serializers.ReadOnlyField(source = 'processo.titulo')
    status = serializers.SerializerMethodField()
    class Meta:
        model = CandidatoProcesso
        fields = ['id','processo','status']
    def get_status(self,obj):
        return obj.get_status_display()

class PerfilSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class ListaUsuarioEmProcessosSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CandidatoProcesso
        fields = '__all__'
        expandable_fields = {
          'perfil': (PerfilSerializer),
          'processo': (ProcessoSeletivoSerializer)
        }