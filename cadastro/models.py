from django.db import models

# Create your models here.
class Cadastro(models.Model):
    
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    age = models.IntegerField()

    def __str__(self):
        return self.firstName