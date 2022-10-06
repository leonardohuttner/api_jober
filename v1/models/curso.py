from email.policy import default
from django.db import models
from uuid import uuid4
from .perfil import Perfil

# Cursos: Nome, descricao, entidade, data, quantidade_horas
class Curso(models.Model):
    modalidades = (('O','Online'),('P','Presencial'))

    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    perfil = models.ForeignKey(Perfil, on_delete= models.CASCADE)
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 100, blank = True)
    entidade = models.CharField(max_length = 100, blank = True)
    modalidade = models.CharField(max_length = 1, choices = modalidades)
    link = models.CharField(max_length = 255, blank = True)
    qtd_horas = models.IntegerField(default = 0)

    def __str__(self):
        return '{} {}'.format(self.nome, self.email)