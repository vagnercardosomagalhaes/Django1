from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    QtdeEstoque = models.IntegerField('Quantidade')


class  Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    tel = models.CharField('Nome',max_length=20)