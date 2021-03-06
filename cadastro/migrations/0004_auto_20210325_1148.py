# Generated by Django 3.0 on 2021-03-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20210324_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcao_voto',
            name='quantidade_votos',
            field=models.IntegerField(default=0, verbose_name='Quantidade de votos'),
        ),
        migrations.AlterField(
            model_name='votacao',
            name='nome_completo',
            field=models.CharField(max_length=194, verbose_name='Nome da votação'),
        ),
    ]
