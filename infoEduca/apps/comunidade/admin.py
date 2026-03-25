from django.contrib import admin
from .models import Topico

@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    search_fields = ('titulo', 'mensagem')