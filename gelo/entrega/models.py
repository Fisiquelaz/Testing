from django.db import models

class Entrega (models.Model):
    nome = models.CharField(max_length=30)
    rua = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    numeroCasa = models.IntegerField()
    complemento = models.CharField(max_length=30)
    qtd = models.IntegerField()
    def __str__(self):
        return self.nome +' '+ self.rua