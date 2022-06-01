from django.db import models

# Create your models here.
class Grupodecontatos(models.Model):

     descricao = models.CharField(max_length=100)


class Contatos(models.Model):

    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        texto = "{0}" "{1}"
        return texto.format(self.nome, self.telefone)

