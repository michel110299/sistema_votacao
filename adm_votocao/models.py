from django.db import models
from cadastro.models import *

class Pessoa_voto(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete = models.CASCADE,
        verbose_name = "Pessoa",
    )
    votacao = models.ForeignKey(
        Votacao,
        on_delete = models.CASCADE,
        verbose_name = "Votação",
    )
    opcao_voto = models.ForeignKey(
        Opcao_voto,
        on_delete = models.CASCADE,
        verbose_name = "Opção de voto",
    )
    quantidade_votos = models.IntegerField(
        verbose_name = "Quantidade de votos",
        default = 0,
    )
    class Meta:
        verbose_name = "votação/eleição"
        verbose_name_plural = "Votações / eleições"
        db_table = "Votacao_eleicao"

    def __str__(self):
        return self.votacao.nome_completo