from django.db import models
from stdimage.models import StdImageField

# Create your models here.
class Base(models.Model):
    criado = models.DateField("Criado", auto_now_add=True)
    modificado = models.DateField("Modificado", auto_now=True)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class BoasVindas(Base):
    imagem = StdImageField("Imagem", upload_to='icons', variations={'thumb': {'width': 1000, 'height':1000}})
    mensagem = models.TextField("Mensagem", max_length=5000)

    class Meta:
        verbose_name = 'Boas Vindas'
        verbose_name_plural = 'Boas Vindas'

    def __str__(self):
        return self.mensagem


class FormacaoAcademica(Base):
    titulo = models.CharField('Titulo', max_length=200)
    instituicao = models.CharField('Instituição', max_length=100)
    conclusao = models.DateField("Conclusão")
    descricao = models.TextField('Descrição', max_length=5000)

    class Meta:
        verbose_name = 'Formação Acadêmica'
        verbose_name_plural = 'Formação Acadêmica'

    def __str__(self):
        return self.titulo
    

class HardSkill(Base):
    icon = StdImageField("Imagem", upload_to='icons', variations={'thumb': {'width': 100, 'height':100}})
    titulo = models.CharField("Título", max_length=100)

    class Meta:
        verbose_name = 'Hard Skill'
        verbose_name_plural = 'Hard Skills'

    def __str__(self):
        return self.titulo
    

class Projeto(Base):
    imagem = StdImageField("Imagem", upload_to='icons', variations={'thumb': {'width': 350, 'height':225}})
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descricao", max_length=500)
    linksite = models.URLField("Link do Site")
    linkgithub = models.URLField("Link GitHub")
    horas = models.IntegerField("Total Horas")

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo
    

class Certificado(Base):
    imagem = StdImageField("Imagem", upload_to='icons', variations={'thumb': {'width': 100, 'height':100}})
    titulo = models.CharField("Título", max_length=100)
    instituicao = models.CharField("Instituição", max_length=200)
    conclusao = models.DateField("Conclusão")
    linkvalida = models.URLField("Link Validação")
    horas = models.IntegerField("Total Horas")

    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'

    def __str__(self):
        return self.titulo