from django.db import models


class Conteudo(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    conteudo_html = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo



class Menu(models.Model):
    TIPO_DESTINO = [
        ('interno', 'Interno'),
        ('externo', 'Externo'),
    ]


    titulo = models.CharField(max_length=150)
    tipo_destino = models.CharField(
        max_length=10,
        choices=TIPO_DESTINO,
    )

    ordem = models.PositiveIntegerField()
    ativo = models.BooleanField(default=True)

    conteudo = models.ForeignKey(
        Conteudo,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    url_externa = models.URLField(blank=True)


    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo
