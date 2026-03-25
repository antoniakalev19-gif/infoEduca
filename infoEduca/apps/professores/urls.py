from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'professor'

urlpatterns = [
    path('', views.dashboard_professor, name='dashboard'),
    path('relatorio/<int:disciplina_id>/', views.relatorio_disciplina, name='relatorio_disciplina'),
    path('novo-material/', views.criar_material, name='criar_material'),
    path('novo-quiz/', views.criar_quiz, name='criar_quiz'),
    path('adicionar-pergunta/<int:atividade_id>/', views.adicionar_pergunta, name='adicionar_pergunta'),
    path("cadastrar/", views.cadastrar_professor, name="cadastrar_professor"),
    path("aguardando-aprovacao/", views.aguardando_aprovacao, name="aguardando_aprovacao"),


    
]