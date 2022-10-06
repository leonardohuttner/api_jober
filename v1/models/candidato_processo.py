from email.policy import default
from django.db import models
from uuid import uuid4

from v1.models.perfil import Perfil
from v1.models.processo_seletivo import ProcessoSeletivo

class CandidatoProcesso(models.Model):
    status = (('1','Aguardando'),('2','Analise'),('3','Retorno'))

    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    processo = models.OneToOneField(ProcessoSeletivo, on_delete= models.CASCADE, null = True)
    perfil = models.ForeignKey(Perfil, on_delete= models.CASCADE, null = True)
    data_canditadura= models.DateTimeField(auto_now_add = True, blank = True)
    retorno = models.TextField(blank = True)
    status = models.CharField(max_length=10, choices = status, default = '1')

    def __str__(self):
        return '{} - {}'.format(self.processo.titulo, self.perfil.usuario.nome)
