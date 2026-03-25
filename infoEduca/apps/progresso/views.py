from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Historico

@login_required
def meu_progresso(request):
    """
    Exibe todas as atividades que o aluno logado já concluiu,
    mostrando as notas e a data.
    """
    # Filtra apenas o histórico do aluno que está acessando a página
    meu_historico = Historico.objects.filter(aluno=request.user).order_by('-data_conclusao')
    
    # Cálculos simples para o painel
    total_atividades = meu_historico.count()
    media_notas = 0
    if total_atividades > 0:
        soma_notas = sum(item.nota for item in meu_historico)
        media_notas = soma_notas / total_atividades

    return render(request, 'progresso/meu_progresso.html', {
        'historico': meu_historico,
        'total': total_atividades,
        'media': media_notas,
    })