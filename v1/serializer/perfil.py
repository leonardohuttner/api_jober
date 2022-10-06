from rest_framework import serializers
from ..models.perfil import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('id','usuario.nome')