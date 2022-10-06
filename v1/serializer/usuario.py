from rest_framework import serializers
from ..models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','nome','sobrenome','email','data_nascimento','cpf','sexo','administrador','ativo']