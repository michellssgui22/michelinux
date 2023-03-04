from django.views.generic import TemplateView
from .models import BoasVindas, FormacaoAcademica, HardSkill, Projeto, Certificado

class IndexViews(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexViews, self). get_context_data(**kwargs)
        context['boasvindas'] = BoasVindas.objects.all()
        context['formacaoacademica'] = FormacaoAcademica.objects.all()
        context['hardskill'] = HardSkill.objects.order_by('?').all()
        context['projetos'] = Projeto.objects.all()
        context['certificado'] = Certificado.objects.all()
        return context


class ContaticViews(TemplateView):
    template_name = 'contato.html'
