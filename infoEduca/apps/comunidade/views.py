from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topico

def mural_comunidade(request):
    # Busca todos os tópicos, do mais recente para o mais antigo
    topicos = Topico.objects.all().order_by('-data_criacao')
    
    # Lógica para postar uma nova dúvida/tópico
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login') # Garante que só logados postem
            
        titulo = request.POST.get('titulo')
        mensagem = request.POST.get('mensagem')
        
        if titulo and mensagem:
            Topico.objects.create(
                titulo=titulo,
                mensagem=mensagem,
                autor=request.user
            )
            return redirect('comunidade:mural')

    return render(request, 'comunidade/mural.html', {'topicos': topicos})