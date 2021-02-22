from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=30)
    data_inicio =models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Artistas"

class Musica(models.Model):
    nome = models.CharField(max_length=50)
    data_Post_Musc = models.DateField(auto_now_add=True)
    duracao = models.PositiveIntegerField()
    artista=models.ForeignKey(Artista,on_delete=models.CASCADE, null=True)
    obesrvacoes=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Musicas"