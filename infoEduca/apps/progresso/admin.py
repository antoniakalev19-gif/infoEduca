from django.contrib import admin
from .models import Historico

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'atividade', 'nota', 'data_conclusao')
    list_filter = ('aluno', 'atividade__disciplina') # Filtra por aluno e pela disciplina da atividade
    search_fields = ('aluno__username', 'atividade__titulo')