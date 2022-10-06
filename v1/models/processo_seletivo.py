from django.db import models
from uuid import uuid4
from .empresa import Empresa

# Projetos: Nome, organizaçcao, data_inicio, data_fim, descricao
class ProcessoSeletivo(models.Model):
    status = (('A','Aberto'),('F','Fechada'),('P','Pausada'))

    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    empresa = models.ForeignKey(Empresa, on_delete= models.CASCADE, null = True)
    titulo = models.CharField(max_length = 80)
    status = models.CharField(max_length = 1, choices = status)
    descricao = models.TextField(max_length = 150)
    candidatos = models.IntegerField(default = 0)
    # etiquetas = models.Charfield()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return '{} - {}'.format(self.empresa.nome, self.titulo)