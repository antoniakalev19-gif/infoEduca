from django.contrib import admin
from apps.disciplinas.models import Disciplina
from apps.atividades.models import Atividade

# Isso cria uma pequena lista de atividades dentro da tela de disciplina
class AtividadeInline(admin.TabularInline):
    model = Atividade
    extra = 1 # Quantidade de linhas vazias para novas atividades

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao')
    inlines = [AtividadeInline] # Adiciona a lista aqui!