# Generated by Django 5.0.2 on 2024-02-08 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(help_text='Informe o seu nome: ', max_length=30)),
                ('cpf', models.CharField(blank=True, help_text='Informe o seu cpf: ', max_length=11, null=True)),
                ('senha', models.CharField(help_text='Informe a sua senha: ', max_length=15)),
                ('telefone', models.CharField(blank=True, help_text='Informe o seu telefone: ', max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
