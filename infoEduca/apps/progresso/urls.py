from django.urls import path
from . import views

app_name = 'progresso'

urlpatterns = [
    #path('', progresso_aluno, name='progresso_aluno'),
    path('', views.meu_progresso, name='meu_progresso'),
]