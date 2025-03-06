from typing import Any

from django.views.generic import ListView, TemplateView , FormView # Do pacóte django.views.generic, estamos importando TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.contrib import messages

#Para usar o TemplateView é só imformar o nome do template

from .models import Servico, Funcionario, Recursos, Clientes
from .forms import ContatoForm

from django.http import JsonResponse


def excluir_dados_usuario(request):
    return JsonResponse({
        "message": "Para solicitar a exclusão de seus dados, envie um e-mail para suporte@seudominio.com com o assunto 'Exclusão de Dados'."
    })


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após registo
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})


class LoginView(TemplateView):
    template_name = 'login.html'

class IndexView(LoginRequiredMixin, ListView):
    models = Funcionario
    template_name =  'index.html'
    paginate_by = 4
    ordering = 'id'
    queryset = Funcionario.objects.order_by('id').all()
    form_class = ContatoForm
    success_url = reverse_lazy('index')



    def get_context_data(self, **kwargs):
        context =  super(IndexView, self).get_context_data(**kwargs)

        context['servicos'] = Servico.objects.order_by('?').all()

        context['clientes'] = Clientes.objects.order_by('?').all()

        context['funcionarios'] = Funcionario.objects.order_by('?').all()

        context['recursos1'] = Recursos.objects.order_by().all()[:3]

        context['recursos2'] = Recursos.objects.order_by().all()[3:]


        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()

        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


