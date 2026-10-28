from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Conteudo, Menu


def _context(conteudo):
    return {
        "conteudo": conteudo,
        "itens_menu": Menu.objects.filter(ativo=True)
        .filter(Q(tipo_destino=Menu.TipoDestino.EXTERNO) | Q(conteudo__ativo=True))
        .select_related("conteudo"),
    }


def inicio(request):
    conteudo_inicial = get_object_or_404(Conteudo, slug="inicio", ativo=True)
    return render(request, "portal/base.html", _context(conteudo_inicial))


def conteudo(request, slug):
    pagina = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, "portal/base.html", _context(pagina))
