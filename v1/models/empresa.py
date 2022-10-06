from django.db import models
from uuid import uuid4
from ..models.usuario import Usuario

class Empresa(models.Model):
    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    usuario = models.OneToOneField(Usuario, on_delete= models.CASCADE, null = True)
    nome = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, blank = True)
    cnpj = models.CharField(max_length = 14)
    cep = models.CharField(max_length = 50, blank = True)
    endereco = models.CharField(max_length = 150, blank = True)
    bairro = models.CharField(max_length = 60,  blank = True)
    cidade = models.CharField(max_length = 60, blank = True)
    estado = models.CharField(max_length = 60, blank = True)
    telefone =  models.CharField(max_length = 60, blank = True)

    def __str__(self):
        return '{}:{}'.format(self.nome, self.cnpj)