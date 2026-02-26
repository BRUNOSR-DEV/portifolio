from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    link_github = models.URLField(max_length=200)
    # Campos novos com a "permissão" para serem vazios no início
    descricao_breve = models.TextField(max_length=200, null=True, blank=True)
    descricao_completa = models.TextField(max_length=1000, null=True, blank=True)
    capa = models.ImageField(upload_to='projetos/capas/', null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class ImagemProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, related_name='imagens', on_delete=models.CASCADE)
    arquivo = models.ImageField(upload_to='projetos/detalhes/')

    def __str__(self):
        return f'Imagem de {self.projeto.nome}'

class Certificado(models.Model):
    titulo_certificado = models.CharField(max_length=150)
    link = models.URLField(max_length=200)
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to='certificados/')

    def __str__(self):
        return self.titulo_certificado