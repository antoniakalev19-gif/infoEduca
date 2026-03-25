from django.urls import path
from . import views

app_name = 'comunidade'

urlpatterns = [
    path('', views.mural_comunidade, name='mural'),
]