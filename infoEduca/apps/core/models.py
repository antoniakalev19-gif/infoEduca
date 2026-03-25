from django.db import models

class BannerHome(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='banners/')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
class MensagemSuporte(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.data_envio.strftime('%d/%m/%Y %H:%M')}"
