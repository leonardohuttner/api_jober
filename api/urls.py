from django.contrib import admin
from django.urls import path, include
from v1.views.contato import ContatoViewSet
from v1.views.empresa import EmpresaViewSet
from v1.views.certificado import CertificadoViewSet
from v1.views.curso import CursoViewSet
from v1.views.projeto import ProjetoViewSet
from v1.views.experiencia import ExperienciaViewSet
from v1.views.educacao import EducacaoViewSet
from v1.views.usuario import UsuarioViewSet
from v1.views.processo_seletivo import ProcessoSeletivoViewSet
from v1.views.candidato_processo import CandidatoProcessoViewSet, ListaProcessoUsuario,ListaUsuariosProcesso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='Usuarios')
router.register('contato', ContatoViewSet, basename='Contato')
router.register('empresa', EmpresaViewSet, basename='Empresa')
router.register('curso', CursoViewSet, basename='Curso')
router.register('educacao', EducacaoViewSet, basename='Educacao')
router.register('experiencia', ExperienciaViewSet, basename='Experiencia')
router.register('projetos', ProjetoViewSet, basename='Projeto')
router.register('certificado', CertificadoViewSet, basename='Certificado')
router.register('processo_seletivo', ProcessoSeletivoViewSet, basename='Processo')
router.register('candidato', CandidatoProcessoViewSet, basename='Candidato')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('usuario/<str:pk>/processos/', ListaProcessoUsuario.as_view()),
    path('processo/<str:pk>/usuarios/', ListaUsuariosProcesso.as_view())
]
