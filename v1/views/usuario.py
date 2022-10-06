from rest_framework import viewsets
from ..models.usuario import Usuario
from ..serializer.usuario import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer