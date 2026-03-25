from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('registrar/', views.registrar, name='registrar'),
    path("suporte/", views.suporte, name="suporte"),

]