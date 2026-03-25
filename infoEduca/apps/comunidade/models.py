from django.db import models
from django.contrib.auth.models import User

class Topico(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título do Tópico")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tópico da Comunidade"
        verbose_name_plural = "Tópicos da Comunidade"

    def __str__(self):
        return self.titulo