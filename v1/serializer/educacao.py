from rest_framework import serializers
from ..models.educacao import  Educacao

class EducacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educacao
        fields = '__all__'
