from django.db import models
from uuid import uuid4
from .usuario import Usuario

#Usuario: Nome, sobrenome, data_nascimento, cpf, sexo, senha, ativo,adm,ultimo_login,criado_em,_atualizaçcao
class Perfil(models.Model):
    id = models.UUIDField(primary_key= True, default = uuid4, editable = False)
    usuario =  models.OneToOneField(Usuario, on_delete= models.CASCADE, null = True)


    def __str__(self):
        return '{} {}'.format(self.usuario.nome,self.usuario.sobrenome)
