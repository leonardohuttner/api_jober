from django.db import models
from uuid import uuid4

#Usuario: Nome, sobrenome, data_nascimento, cpf, sexo, senha, ativo,adm,ultimo_login,criado_em,_atualizaçcao
class Usuario(models.Model):
    SEXO_CHOICE = (('F','Feminino'),('M', 'Masculino'),('O', 'Outro'))
    
    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    #perfil = models.ForeignKey('Perfil', on_delete= models.CASCADE, null=True)
    nome = models.CharField(max_length = 50)
    sobrenome = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    data_nascimento = models.DateField(null= True)
    cpf = models.CharField(max_length = 11)
    sexo = models.CharField(max_length = 1, choices = SEXO_CHOICE)
    senha = models.CharField(max_length = 255)
    ativo = models.BooleanField(default = True)
    administrador = models.BooleanField(default = False)
    ultimo_login = models.DateField(null= True, blank = True)
    criado_em = models.DateTimeField(auto_now_add = True, blank = True)
    atualizado_em = models.DateTimeField(auto_now = True,  blank = True)

    def __str__(self):
        return '{} {}'.format(self.nome, self.email)
