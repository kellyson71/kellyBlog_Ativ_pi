# Generated by Django 5.1.3 on 2024-12-03 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, verbose_name='Cadastro de Pessoa Física'),
        ),
    ]
