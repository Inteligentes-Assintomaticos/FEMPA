from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Conteudo(models.Model):
    titulo = models.CharField("título", max_length=120)
    slug = models.SlugField("slug", max_length=140, unique=True)
    html = models.TextField("conteúdo HTML", help_text="Informe apenas o HTML interno da página, sem html, head, body, header, nav ou footer.")
    ativo = models.BooleanField("ativo", default=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "conteúdo"
        verbose_name_plural = "conteúdos"

    def __str__(self):
        return self.titulo


class Menu(models.Model):
    class TipoDestino(models.TextChoices):
        INTERNO = "interno", "Conteúdo interno"
        EXTERNO = "externo", "Link externo"

    titulo = models.CharField("título", max_length=120)
    tipo_destino = models.CharField("tipo de destino", max_length=10, choices=TipoDestino.choices)
    ordem = models.PositiveIntegerField("ordem", default=0)
    ativo = models.BooleanField("ativo", default=True)
    conteudo = models.ForeignKey(
        Conteudo, verbose_name="conteúdo relacionado", on_delete=models.CASCADE,
        null=True, blank=True, related_name="itens_menu",
    )
    url_externa = models.URLField("URL externa", blank=True)

    class Meta:
        ordering = ["ordem", "id"]
        verbose_name = "item do menu"
        verbose_name_plural = "itens do menu"

    def __str__(self):
        return self.titulo

    def clean(self):
        errors = {}
        if self.tipo_destino == self.TipoDestino.INTERNO:
            if not self.conteudo:
                errors["conteudo"] = "Selecione o conteúdo interno deste item."
            if self.url_externa:
                errors["url_externa"] = "Links internos não usam URL externa."
        elif self.tipo_destino == self.TipoDestino.EXTERNO:
            if not self.url_externa:
                errors["url_externa"] = "Informe a URL do link externo."
            if self.conteudo:
                errors["conteudo"] = "Links externos não se relacionam com conteúdo interno."
        if errors:
            raise ValidationError(errors)

    def get_absolute_url(self):
        if self.tipo_destino == self.TipoDestino.INTERNO and self.conteudo_id:
            if self.conteudo.slug == "inicio":
                return reverse("inicio")
            return reverse("conteudo", kwargs={"slug": self.conteudo.slug})
        return self.url_externa
