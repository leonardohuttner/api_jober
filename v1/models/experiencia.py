from django.db import models
from uuid import uuid4
from v1.models.perfil import Perfil
# Experianecia: Cargo, empresa, data_inicio, data_fim, descricao

class Experiencia(models.Model):
    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    perfil = models.ForeignKey(Perfil, on_delete= models.CASCADE, null = True)
    cargo = models.BooleanField(default = False)
    empresa = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 50)
    data_inicio = models.DateField()
    data_fim = models.DateField()

