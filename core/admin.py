from django.contrib import admin

from .models import Produto, Contato

class ProdutoAdmin(admin.ModelAdmin):
    list_display    =   ('nome', 'preco', 'QtdeEstoque')


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tel') 



admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Contato, ContatoAdmin)
