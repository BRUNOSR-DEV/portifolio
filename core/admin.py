from django.contrib import admin
from .models import Projeto, Certificado, ImagemProjeto, Habilidade

class ImagemProjetoInline(admin.TabularInline):
    model = ImagemProjeto
    extra = 3

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'link_github') # Barra de visualização 
    inlines = [ImagemProjetoInline]
    search_fields = ('nome', 'categoria') 

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo_certificado',)

@admin.register(Habilidade)
class HabilidadeAdmin(admin.ModelAdmin):
    list_display = ('titulo_hab',)