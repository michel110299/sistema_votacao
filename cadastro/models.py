from django.db import models

class Pessoa(models.Model):

    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194,
    )

    cpf = models.CharField(
        verbose_name= "CPF",
        max_length = 14,
        
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False,
    )
    email = models.EmailField(
        verbose_name="E-mail",
        max_length = 194,
        unique = True,
        null = True,
        blank = True,
    )
    horario_criacao = models.DateTimeField(
        verbose_name= "Horário de criação",
        auto_now_add = True,
        null = True,
        blank = True,
    )
    class Meta:
        verbose_name = "Pessoa"
        db_table = "pessoa"

    def __str__(self):
        return self.nome_completo

class Votacao(models.Model):

    nome_completo = models.CharField(
        verbose_name = "Nome da votação",
        max_length = 194,
    )
    descricao = models.TextField(
        verbose_name = "Descricao",
        max_length = 350,
    )
    anonimo = models.BooleanField(
        verbose_name = "Anônimo",
    )
    voto_unico = models.BooleanField(
        verbose_name = "Voto unico",
    )
    horario_inicio = models.DateTimeField(
        verbose_name="",
        auto_now= False,
        blank = True, 
        null = True,
    )
    horario_termino = models.DateTimeField(
        verbose_name="",
        auto_now= False,
        blank = True, 
        null = True,
    )
    horario_criacao = models.DateTimeField(
        verbose_name= "Horário de criação",
        auto_now_add = True,
    )
    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"
        db_table = "votacao"

    def __str__(self):
        return self.nome_completo

class Opcao_voto(models.Model):

    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194,
    )

    votacao = models.ForeignKey(
        Votacao,
        on_delete = models.CASCADE,
        verbose_name = "Votação de participação",
    )
    codigo_votacao = models.CharField(
        verbose_name = "Codigo da votação ",
        max_length = 194,
    )
    quantidade_votos = models.IntegerField(
        verbose_name = "Quantidade de votos",
        default = 0,
    )
    class Meta:
        verbose_name = "Opcão de voto"
        verbose_name_plural = "Opções de voto "
        db_table = "Opcao_de_voto"

    def __str__(self):
        return self.nome_completo


    
