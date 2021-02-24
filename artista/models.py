from django.db import models
from django.db import migrations, models


class Artista(models.Model):
    nome = models.CharField(max_length=30)
    data_inicio =models.DateField(null=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Artistas"

class Musica(models.Model):
    nome = models.CharField(max_length=50)
    data_Post_Musc =models.DateField(null=True)
    duracao = models.PositiveIntegerField()
    youtube= models.BooleanField( default=False)
    spotify=models.BooleanField (default =False)
    # songs permite acesso as musicas do artista
    artista=models.ForeignKey(Artista, related_name='musicas', on_delete=models.CASCADE, null=True)
    obesrvacoes=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Musicas"