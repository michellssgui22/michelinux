from django.contrib import admin
from .models import BoasVindas, FormacaoAcademica, HardSkill, Projeto, Certificado

# Register your models here.
@admin.register(BoasVindas)
class BoasVindasAdmin(admin.ModelAdmin):
    list_display = ('mensagem', 'modificado', 'ativo')


@admin.register(FormacaoAcademica)
class FormacaoAcademicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'conclusao', 'descricao', 'modificado', 'ativo')


@admin.register(HardSkill)
class HardeSkillAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'modificado', 'ativo')


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'linksite', 'linkgithub', 'modificado', 'ativo')


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'conclusao', 'linkvalida', 'modificado', 'ativo')