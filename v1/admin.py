from atexit import register
from django.contrib import admin
from v1.models.contato import Contato
from .models.empresa import Empresa
from .models.usuario import Usuario
from .models.certificado import Certificado
from .models.curso import Curso
from .models.educacao import Educacao
from .models.experiencia import Experiencia
from .models.projeto import Projeto
from .models.candidato_processo import CandidatoProcesso
from .models.processo_seletivo import ProcessoSeletivo
from .models.perfil import Perfil

# Register your models here.
class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome','criado_em')
    list_display_links = ('id', 'nome')

admin.site.register(Usuario, Usuarios)

class Contatos(admin.ModelAdmin):
    list_display = ('id', 'cidade', 'estado')


admin.site.register(Contato, Contatos)

class Empresas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj')
    list_display_links = ('id', 'nome', 'cnpj')
    search_fields = ('id','cnpj')

admin.site.register(Empresa, Empresas)

admin.site.register(Certificado)
admin.site.register(Curso)
admin.site.register(Educacao)
admin.site.register(Experiencia)
admin.site.register(Projeto)
admin.site.register(CandidatoProcesso)

class Processos(admin.ModelAdmin):
    list_display = ('id','titulo','status','candidatos')
    list_display_links = ('id', 'titulo')

admin.site.register(ProcessoSeletivo,Processos)

class Perfis(admin.ModelAdmin):
    list_display = ('id','usuario')

admin.site.register(Perfil,Perfis)