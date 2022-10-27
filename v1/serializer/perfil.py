from rest_framework import serializers
from ..models.perfil import Perfil
from ..models.usuario import Usuario

class PerfilSerializer(serializers.ModelSerializer):
    usuario = Usuario.objects.select_related('usuario')
    class Meta:
        model = Perfil
        fields = ('id','usuario')
        # expandable_fields = {
        #   'usuario': (Usuario)
        # }