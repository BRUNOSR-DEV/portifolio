from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    link_github = models.URLField(max_length=200)
    descricao = models.TextField(max_length=500)
    # Usando ImageField (Recomendado para Django)
    imagem = models.ImageField(upload_to='projetos/') 

    def __str__(self):
        return self.nome

class Certificado(models.Model):
    titulo_certificado = models.CharField(max_length=150)
    link = models.URLField(max_length=200)
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to='certificados/')

    def __str__(self):
        return self.titulo_certificado
