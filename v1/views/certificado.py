from rest_framework import viewsets
from ..models.certificado import Certificado
from ..serializer.certificado import CertificadoSerializer

class CertificadoViewSet(viewsets.ModelViewSet):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer