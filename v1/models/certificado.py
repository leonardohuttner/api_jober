from django.db import models
from uuid import uuid4
from v1.models.perfil import Perfil

# Certificados: Nome, Descricao, Local curso, Ano, Link
class Certificado(models.Model):
    modalidades = (('O','Online'),('P','Presencial'))
    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    perfil = models.ForeignKey(Perfil, on_delete= models.CASCADE)
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 100, blank = True)
    local = models.CharField(max_length = 100, blank = True)
    modalidade = models.CharField(max_length = 1, choices = modalidades)
    link = models.CharField(max_length = 255, blank = True)

    def __str__(self):
        return '{} {}'.format(self.nome, self.email)