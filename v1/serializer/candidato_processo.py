from rest_framework import serializers
from v1.models.perfil import Perfil
import json

from ..models.candidato_processo import  CandidatoProcesso

class CandidatoProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatoProcesso
        fields = '__all__'

class ListaProcessoUsuarioSerializer(serializers.ModelSerializer):
    processo = serializers.ReadOnlyField(source = 'processo.titulo')
    status = serializers.SerializerMethodField()
    class Meta:
        model = CandidatoProcesso
        fields = ['id','processo','status']
    def get_status(self,obj):
        return obj.get_status_display()

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id', 'perfil.usuario.nome']

class ListaUsuarioEmProcessosSerializer(serializers.ModelSerializer):
    # perfil = serializers.ReadOnlyField(source = 'perfil.usuario')
    perfil = serializers.SerializerMethodField()
    class Meta:
        model = CandidatoProcesso
        fields = ['perfil']
    def get_perfil(self,obj):
        return obj.perfil.usuario.nome