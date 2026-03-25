from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Atividade
from apps.progresso.models import Historico


@login_required
def atividades_home(request):
    atividades = Atividade.objects.all().select_related('disciplina')
    
    # Criamos um dicionário com as notas que o aluno já tirou
    # Ex: {id_da_atividade: nota}
    historico_aluno = Historico.objects.filter(aluno=request.user).values_list('atividade_id', 'nota')
    notas_dict = {at_id: nota for at_id, nota in historico_aluno}

    # Adicionamos a nota diretamente no objeto da atividade antes de enviar para o template
    for atividade in atividades:
        atividade.nota_aluno = notas_dict.get(atividade.id)

    return render(request, 'atividades/index.html', {'atividades': atividades})

def detalhe_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    
    if request.method == "POST" and atividade.tipo == 'quiz':
        perguntas = atividade.perguntas.all()
        acertos = 0
        total = perguntas.count()
        erros = []  # 🔹 lista para guardar os erros
        
        for pergunta in perguntas:
            resposta_aluno = request.POST.get(f'pergunta_{pergunta.id}')
            if resposta_aluno == pergunta.resposta_correta:
                acertos += 1
            else:
                # 🔹 adiciona na lista de erros
                erros.append({
                    "questao": pergunta.enunciado,              # texto da questão
                    "resposta_usuario": resposta_aluno,     # resposta escolhida
                    "resposta_correta": pergunta.resposta_correta,  # resposta correta
                })
        
        # --- SALVAR NO HISTÓRICO ---
        if request.user.is_authenticated:
            nota_final = (acertos / total) * 10 if total > 0 else 0
            Historico.objects.update_or_create(
                aluno=request.user, 
                atividade=atividade,
                defaults={'nota': nota_final, 'completado': True}
            )
        # ---------------------------

        return render(request, 'atividades/resultado.html', {
            'atividade': atividade,
            'acertos': acertos,
            'total': total,
            'erros': erros  # 🔹 passa a lista para o template
        })
    
    # Lógica para carregar a página (Método GET)
    context = {'atividade': atividade}
    
    if atividade.tipo == 'quiz':
        context['perguntas'] = atividade.perguntas.all()
        return render(request, 'atividades/quiz.html', context)
    
    return render(request, 'atividades/material.html', context)