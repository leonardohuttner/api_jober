from rest_framework import serializers
from ..models.certificado import  Certificado

class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = '__all__'
