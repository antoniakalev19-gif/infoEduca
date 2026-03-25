from django.urls import path
from . import views

app_name = 'disciplinas'

urlpatterns = [
    path('', views.lista_disciplinas, name='lista_disciplinas'),
    path('<int:disciplina_id>/', views.detalhe_disciplina, name='detalhe_disciplina'),
]