from django.db import models

# Modelos
class Funcionarios(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=255, null=False, blank=False)
    tempo_de_serviço = models.PositiveBigIntegerField(default=0, null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    # O campo objetos = models.Manager() é utilizado para fazer operações de busca
    objetos = models.Manager()

    # Portanto, toda vez que você alterar um arquivo de modelo, não se
    # esqueça de executar python manage.py makemigrations!

