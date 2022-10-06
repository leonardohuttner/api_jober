from rest_framework import viewsets
from ..models.contato import Contato
from ..serializer.contato import ContatoSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer