from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} descricao: {self.descricao}"
    
class Cartao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento_fatura = models.PositiveSmallIntegerField(validators=([MinValueValidator(1), MaxValueValidator(31)]))
    fechamento_fatura = models.PositiveSmallIntegerField(validators=([MinValueValidator(1), MaxValueValidator(31)]))

class Transacao(models.Model):
    TIPOS_TRANSACAO = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transacoes', null=False)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(choices=TIPOS_TRANSACAO)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default='sem categoria')
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - R${self.valor} em {self.data}"

