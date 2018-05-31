from django.db import models

# Create your models here.
CH_CAT = [
    ('1','Categoria 1'),
    ('2','Categoria 2'),
    ('3','Categoria 3'),
    ('4','Categoria 4')
]

class Cooperativa(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    municipio = models.CharField(max_length=100, help_text='Informe o município da sede da cooperativa')
    categoria = models.CharField(max_length=100, choices=CH_CAT)
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return "%s - %s" % (self.nome, self.municipio)


class Galpao(models.Model):
    capacidade = models.PositiveIntegerField(help_text='Em kg. Ex: 2000 para 2 toneladas de capacidade')
    endereco = models.CharField(max_length=100, help_text='Informe o endereço')
    categoria = models.CharField(max_length=100, choices=CH_CAT)
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)
    cooperativa = models.ForeignKey(Cooperativa, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.cooperativa, self.endereco)




class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço (R$)', help_text='Preço por quilograma')
    validade = models.PositiveIntegerField(verbose_name='Tempo de validade', help_text='Tempo dado em dias')
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "%s - %s" % (self.nome, self.preco)


class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    galpao = models.ForeignKey(Galpao, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(help_text='Em kg. Ex: 2000 para 2 toneladas do produto')
    ultima_atualizacao = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "%s - %s" % (self.produto, self.quantidade)
