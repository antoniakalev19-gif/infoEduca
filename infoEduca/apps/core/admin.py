from django.contrib import admin
from .models import MensagemSuporte


@admin.register(MensagemSuporte)
class MensagemSuporteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "mensagem", "data_envio")  # campos que existem no modelo
    search_fields = ("nome", "email", "mensagem")               # busca por nome, email ou mensagem
    list_filter = ("data_envio",)