from django.db import models
from django.contrib.auth.models import User
from apps.atividades.models import Atividade

class Historico(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Estudante")
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    data_conclusao = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Histórico de Progresso"
        verbose_name_plural = "Histórico de Progresso"

    def __str__(self):
        return f"{self.aluno.username} - {self.atividade.titulo}"