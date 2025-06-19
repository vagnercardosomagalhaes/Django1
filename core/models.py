from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    QtdeEstoque = models.IntegerField('Quantidade')

    def __str__(self):
        return f'{self.nome}'
        


class  Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    tel = models.CharField('Telefone',max_length=20)

    def __str__(self):
        return f'{self.nome}'
        