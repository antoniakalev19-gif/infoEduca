
from django.shortcuts import render, get_object_or_404
from .models import Disciplina
from apps.progresso.models import Historico # Importe o seu modelo de histórico

def index(request):
    disciplinas = Disciplina.objects.all()
    historico_recente = []
    
    if request.user.is_authenticated:
        # Puxa o histórico do aluno logado (independente de professor ou não)
        historico_recente = Historico.objects.filter(aluno=request.user).order_by('-data_conclusao')[:5]
    
    return render(request, 'index.html', {
        'disciplinas': disciplinas,
        'historico': historico_recente
    })

def lista_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplinas/lista.html', {'disciplinas': disciplinas})

def detalhe_disciplina(request, disciplina_id):
    # Busca a disciplina ou retorna erro 404 se não existir
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    
    # Filtramos as atividades usando o related_name='atividades' que você criou no Model
    materiais = disciplina.atividades.filter(tipo='material')
    quizzes = disciplina.atividades.filter(tipo='quiz')
    
    return render(request, 'disciplinas/detalhe.html', {
        'disciplina': disciplina,
        'materiais': materiais,
        'quizzes': quizzes,
        'tem_conteudo': materiais.exists() or quizzes.exists()
    })