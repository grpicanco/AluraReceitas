from django.db import models


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
        null=True,
        default=True,
    )

    class Meta:
        abstract = True


class Pessoa(BaseModels):
    nome = models.CharField(
        db_column='tx_nome',
        null=False,
        blank=False,
        max_length=200,
    )
    email = models.CharField(
        db_column='tx_email',
        null=False,
        blank=False,
        max_length=200,
    )
    dt_nascimento = models.DateTimeField(
        db_column='dt_nascimento',
        null=False,
    )

    def __str__(self):
        return self.nome
