from django.db import models

# Create your models here.
class Cadastro(models.Model):
    """classe responsável por definir dentro do banco de dados
    os campos relacionados a função de cadastro de usuários"""

    user_name = models.CharField(max_length=30, blank=False, help_text='Informe o seu nome: ')
    cpf = models.CharField(max_length=11, blank=True, null=True,help_text='Informe o seu cpf: ')
    senha = models.CharField(max_length=15, blank=False, help_text='Informe a sua senha: ')
    telefone = models.CharField(max_length=20, blank=True, null=True, help_text='Informe o seu telefone: ')
    email = models.EmailField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        #retornará o nome do usuario
        return self.user_name