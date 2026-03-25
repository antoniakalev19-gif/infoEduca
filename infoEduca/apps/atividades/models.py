from django.db import models
from apps.disciplinas.models import Disciplina

class Atividade(models.Model):
    TIPO_CHOICES = [
        ('material', 'Material de Estudo (PDF/Link)'),
        ('quiz', 'Quiz Interativo'),
    ]

    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='atividades')
    titulo = models.CharField(max_length=200, verbose_name="Título")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='material')
    
    # Para Material de Estudo
    descricao = models.TextField(blank=True, verbose_name="Instruções ou Resumo")
    arquivo = models.FileField(upload_to='materiais/', null=True, blank=True, verbose_name="Arquivo PDF/Material")
    link_video = models.URLField(null=True, blank=True, verbose_name="Link de Vídeo Aula (YouTube)")

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"

    def __str__(self):
        return self.titulo

# Nova classe para as perguntas do Quiz
class Pergunta(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='perguntas')
    enunciado = models.TextField()
    opcao_a = models.CharField(max_length=255)
    opcao_b = models.CharField(max_length=255)
    opcao_c = models.CharField(max_length=255)
    opcao_d = models.CharField(max_length=255)
    resposta_correta = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return f"Pergunta de: {self.atividade.titulo}"