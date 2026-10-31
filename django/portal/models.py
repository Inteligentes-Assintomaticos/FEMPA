from django.db import models


class Conteudo(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    conteudo_html = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
