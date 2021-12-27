from django.db import models
from pessoas.models import Pessoa


# Create your models here.

class BaseModels(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True
    )
    criado_em = models.DateTimeField(
        db_column='dt_criacao',
        auto_now_add=True,
    )
    modificado_em = models.DateTimeField(
        db_column='dt_modificado',
        auto_now_add=True,
    )
    ativo = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
    )

    class Meta:
        abstract = True


class Receita(BaseModels):
    nome_receita = models.CharField(
        db_column='tx_nome_receita',
        null=False,
        blank=False,
        max_length=200,
    )
    ingredientes = models.TextField(
        db_column='tx_ingredientes',
        null=False,
        blank=False,
    )
    modo_preparo = models.TextField(
        db_column='tx_modo_preparo',
        null=False,
        blank=False,
    )
    tempo_preparo = models.IntegerField(
        db_column='nb_tempo_preparo',
        null=False,
        blank=False,
    )
    rendimento = models.CharField(
        db_column='tx_rendimento',
        null=False,
        blank=False,
        max_length=100,
    )
    categoria = models.CharField(
        db_column='tx_categoria',
        null=False,
        blank=False,
        max_length=100,
    )
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        db_column='id_pessoa',
    )
    img = models.ImageField(
        upload_to='fotos/%d/%m/%Y',
        blank=True,

    )

    def __str__(self):
       return self.nome_receita
