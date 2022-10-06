from django.db import models
from apps.pessoa.models import Pessoa

# Create your models here.
class Animal(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=30)
    #idade = models.IntegerField(blank=True, null=True) # assim não tem nenhum valor
    #idade = models.IntegerField(default=0)# coloca idade automaticamente
    idade = models.IntegerField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        #return self.nome
        #return f'{self.especie}: {self.nome} / idade: {self.idade} anos'
        return f'{self.especie}: {self.nome}'