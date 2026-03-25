from django.urls import path
from . import views

app_name = 'atividades'

urlpatterns = [
    path('', views.atividades_home, name='atividades_home'),
    path('<int:atividade_id>/', views.detalhe_atividade, name='detalhe_atividade'),
  

]