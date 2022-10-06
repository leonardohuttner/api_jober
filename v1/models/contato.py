from django.db import models
from uuid import uuid4
from v1.models.perfil import Perfil
#Contato:  telefone, site pessoal, linkedin, estado, cidade, endereço
class Contato(models.Model):
    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    perfil = models.OneToOneField(Perfil, on_delete= models.CASCADE, null = True)
    deficiencia = models.BooleanField(default = False)
    cep = models.CharField(max_length = 50)
    endereco = models.CharField(max_length = 150)
    bairro = models.CharField(max_length = 60, blank = True)
    cidade = models.CharField(max_length = 60)
    estado = models.CharField(max_length = 60)
    telefone =  models.CharField(max_length = 60)
    site_pessoal = models.CharField(max_length = 150, blank = True)
    linkedin = models.CharField(max_length = 150, blank = True)
    github = models.CharField(max_length = 150, blank = True)
