from django.db import models
from django.contrib.auth.models import User

class Transacao(models.Model):
    TIPOS_TRANSACAO = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas', null=False)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(choices=TIPOS_TRANSACAO)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - R${self.valor} em {self.data}"
