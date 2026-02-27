from django.shortcuts import render
from .models import Projeto, Certificado, Habilidade

from django.views.generic import TemplateView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name =  'index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['projetos'] = Projeto.objects.all() 

        context['certificados'] = Certificado.objects.all()


        context['habilidades'] = Habilidade.objects.all()



        return context
