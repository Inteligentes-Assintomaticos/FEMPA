from django.contrib import admin
from .models import Conteudo, Menu


class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('titulo', 'slug')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_destino', 'ordem', 'ativo')
    list_filter = ('tipo_destino', 'ativo')
    search_fields = ('titulo',)


admin.site.register(Conteudo, ConteudoAdmin)
admin.site.register(Menu, MenuAdmin)
