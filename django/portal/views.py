from django.shortcuts import get_object_or_404, render, redirect
from .models import Conteudo, Menu



def itens_ativos():
    return Menu.objects.filter(ativo=True).select_related('conteudo')


def home(request):
    conteudo = get_object_or_404(       #* Atribuindo o registro `inicio` a variável `conteudo`
        Conteudo,
        slug="inicio",
        ativo=True,
    )

    return render(
        request,
        "portal/home.html",
        {
            "conteudo": conteudo,
            'menu': itens_ativos(),
        },
    )



def conteudo(request, slug):
    if slug == 'inicio':
        return redirect('portal:Home')

    
    pagina = get_object_or_404(
        Conteudo,
        slug=slug,
        ativo=True,
    )

    return render(
        request,
        "portal/conteudo.html",
        {
            'conteudo': pagina,
            'menu': itens_ativos(),
        },
    )
