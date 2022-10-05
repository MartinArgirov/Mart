from django.db import models

# Create your models here.
class Despesa(models.Model):
    despesa = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    valor = models.CharField(max_length=10)
    data = models.IntegerField()
    mes = models.IntegerField()
    #idade = models.IntegerField(blank=True, null=True) # assim não tem nenhum valor
    #idade = models.IntegerField(default=0)# coloca idade automaticamente
    

    def __str__(self):
        #return self.valor
        #return f'{self.mes}: {self.valor}: {self.categoria}'
        return f'{self.mes}: {self.valor}'