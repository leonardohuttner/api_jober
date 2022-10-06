from rest_framework import viewsets
from ..models.empresa import Empresa
from ..serializer.empresa import EmpresaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
