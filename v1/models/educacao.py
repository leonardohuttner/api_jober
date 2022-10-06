from django.db import models
from uuid import uuid4
from v1.models.perfil import Perfil
# Educaçao: Nivel, Escola, Cidade, Ano_final
class Educacao(models.Model):
    nivel = (
        ('FI','Fundamental Incompleto'),
        ('FC','Fundamental Completo'),
        ('MI','Medio Incompleto'),
        ('MC','Medio Completo'),
        ('SI','Superior Incompleto'),
        ('SC','Superior Completo'),
        ('MSI','Mestrado Incompleto'),
        ('MSC','Mestrado Completo'),
        ('DRI','Doutorado Incompleto'),
        ('DRC','Doutorado Completo'),
        )

    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    perfil = models.ForeignKey(Perfil, on_delete= models.CASCADE, null = True)
    nivel = models.CharField(max_length = 3, choices = nivel)
    nome = models.CharField(max_length = 50)
    cidade = models.CharField(max_length = 150)
    data_fim = models.DateField()