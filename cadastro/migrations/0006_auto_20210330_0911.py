# Generated by Django 3.0 on 2021-03-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20210329_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name='CPF'),
        ),
    ]