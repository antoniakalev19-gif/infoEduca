from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default="sememail@exemplo.com")
    escola = models.CharField(max_length=150, default="Não informado")  
    ano_graduacao = models.PositiveIntegerField(default=2000) 
    area = models.CharField(max_length=100, default="Não informado")  
    especialidade = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='professores/', null=True, blank=True)
    bio = models.TextField(blank=True)
    aprovado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Professores"

    def __str__(self):
        return self.nome