from django.db import models
from django.utils.timezone import now

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField(default=now())
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.IntegerField(default=1, max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural ="Transações"

    def __str__(self):
        return self.descricao