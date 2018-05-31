from django.contrib.auth.models import User
from django.db import models

# Create your models here.
CH_CAT = [
    ('1','Categoria 1'),
    ('2','Categoria 2'),
    ('3','Categoria 3'),
    ('4','Categoria 4')
]

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=30, verbose_name='CNPJ', null=True, blank=True)
    data_criacao = models.DateField(auto_now_add=True)
    municipio = models.CharField(max_length=100, help_text='Informe o município da sede da empresa')
    categoria = models.CharField(max_length=100, choices=CH_CAT)
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return "%s - %s" % (self.nome, self.municipio)


class Fabrica(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=100, help_text='Informe o endereço')

    categoria = models.CharField(max_length=100, choices=CH_CAT)
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return "%s - %s" % (self.empresa, self.endereco)




class Produto(models.Model):
    nome = models.CharField(max_length=100)
    validade = models.PositiveIntegerField(verbose_name='Tempo de validade', help_text='Tempo dado em dias')
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "%s" % (self.nome)


class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)
    necessidade = models.PositiveIntegerField(verbose_name='Necessidade média mensal (kg)',
                                              help_text='Ex: 2000 para 2 toneladas do produto', default=1000)
    minimo = models.PositiveIntegerField(verbose_name='Volume mínimo necessário (kg)',
                                         help_text='Ex: 2000 para 2 toneladas do produto', default=100)
    maximo = models.PositiveIntegerField(verbose_name='Volume máximo suportado (kg)',
                                         help_text='Ex: 2000 para 2 toneladas do produto', default=3000)
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade atual em estoque (kg)',
                                             help_text='Ex: 2000 para 2 toneladas do produto', default=700)
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "%s - %s" % (self.produto, self.quantidade)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Estoque"


class Funcionario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "%s - %s" % (self.usuario, self.empresa)

