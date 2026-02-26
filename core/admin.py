from django.contrib import admin
from .models import Projeto, Certificado, ImagemProjeto

class ImagemProjetoInline(admin.TabularInline):
    model = ImagemProjeto
    extra = 3

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'link_github') # Colunas que aparecem na lista
    inlines = [ImagemProjetoInline]
    search_fields = ('nome', 'categoria') # Barra de busca

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo_certificado',)