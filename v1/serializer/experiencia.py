from rest_framework import serializers
from ..models.experiencia import  Experiencia

class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia
        fields = '__all__'
