from django.urls import path
from . import views


app_name = "portal"

urlpatterns = [
    path("", views.home, name="Home"),
    path(
        "conteudo/<slug:slug>/",     #* o django preenche automaticamente o <slug:slug> pelo correspondente
        views.conteudo,
        name='conteudo',
    ),

]
