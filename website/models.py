from django.db import models

# Modelos
class Funcionarios(models.MOdel):
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=255, null=False, blank=False)
    tempo_de_serviço = models.IntegerField(default=0, null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)


