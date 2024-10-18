from django.db import models
# Create your models here.

class Produto(models.Model):
    # codigoProduto = models.CharField(max_length=255) # Campo de char, máximo de 255
    tituloProduto = models.CharField(max_length=255) # Campo de char, máximo de 255
    preco = models.DecimalField(max_digits=10, decimal_places=2) # Campo de decimal (float), máximo de digitos de 10 e de decimal é 2
    descricao = models.TextField(max_length=255) # Campo de char, máximo de 255
    imgProduto = models.CharField(max_length=255) # Campo de char, máximo de 255
    catProduto = models.CharField(max_length=255) # Campo de char, máximo de 255
    classProduto = models.DecimalField(max_digits=2, decimal_places=1) # Campo de decimal (float), máximo de digitos de 10 e de decimal é 2
    exibirHome = models.BooleanField(default=True) #Campo booleano, padrão dele é True (verdadeiro)

