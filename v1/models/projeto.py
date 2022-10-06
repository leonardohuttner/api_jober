from django.db import models
from uuid import uuid4
from v1.models.perfil import Perfil
# Projetos: Nome, organizaçcao, data_inicio, data_fim, descricao
class Projeto(models.Model):
    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    perfil = models.ForeignKey(Perfil, on_delete= models.CASCADE, null = True)
    nome = models.CharField(max_length = 50)
    organizacao = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 150)
    data_inicio = models.DateField()
    data_fim = models.DateField()
