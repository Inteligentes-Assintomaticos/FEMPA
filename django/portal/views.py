from django.shortcuts import get_object_or_404, render
from .models import Conteudo


def home(request):
    conteudo = get_object_or_404(       #* Atribuindo o registro `inicio` a variável `conteudo`
        Conteudo,
        slug="inicio",
        ativo=True,
    )

    return render(
        request,
        "portal/home.html",
        {"conteudo": conteudo},     #* Atribuição da variável `conteudo` ao nome "conteudo" --> usado posteriormente no template `home.html`
    )
