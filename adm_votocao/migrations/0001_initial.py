# Generated by Django 3.0 on 2021-03-24 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0003_auto_20210324_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa_voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_votos', models.IntegerField(verbose_name='Quantidade de votos')),
                ('opcao_voto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Opcao_voto', verbose_name='Opção de voto')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Pessoa', verbose_name='Pessoa')),
                ('votacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Votacao', verbose_name='Votação')),
            ],
            options={
                'verbose_name': 'votação/eleição',
                'verbose_name_plural': 'Votações / eleições',
                'db_table': 'Votacao_eleicao',
            },
        ),
    ]
