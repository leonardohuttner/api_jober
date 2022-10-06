from rest_framework import serializers
from ..models.processo_seletivo import ProcessoSeletivo

class ProcessoSeletivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessoSeletivo
        fields = ('id','titulo')