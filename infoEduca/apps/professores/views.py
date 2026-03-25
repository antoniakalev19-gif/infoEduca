from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from apps.progresso.models import Historico
from apps.disciplinas.models import Disciplina
from apps.atividades.models import Atividade, Pergunta 
from .forms import ProfessorForm
from django.contrib import messages
from functools import wraps

#adicionei esse trecho para cadasrtar professor
def cadastrar_professor(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST, request.FILES)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.aprovado = False
            professor.save()
            messages.success(request, "Cadastro enviado! Aguarde aprovação do administrador.")
            return redirect("professor:aguardando_aprovacao")
        else:
            # 🔹 Mostra os erros do formulário
            print(form.errors)  # aparece no terminal
            messages.error(request, f"Erro no cadastro: {form.errors}")
    else:
        form = ProfessorForm()
    return render(request, "professor/cadastrar.html", {"form": form})


def professor_aprovado_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # 🔹 Verifica se está logado e tem perfil de professor
        if not request.user.is_authenticated or not hasattr(request.user, "professor"):
            messages.error(request, "Você precisa estar logado como professor.")
            return redirect("login")

        professor = request.user.professor

        # 🔹 Bloqueia se não estiver aprovado
        if not professor.aprovado:
            messages.warning(request, "Seu cadastro ainda não foi aprovado pelo administrador.")
            return redirect("professor:aguardando_aprovacao")

        # 🔹 Se aprovado, segue normalmente
        return view_func(request, *args, **kwargs)

    return _wrapped_view

def aprovar_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    professor.aprovado = True
    professor.save()
    messages.success(request, f"O professor {professor.nome} foi aprovado com sucesso!")
    return redirect("professor:lista_professores")

def lista_professores(request):
    professores = Professor.objects.all()
    return render(request, "professor/lista.html", {"professores": professores})


 

@staff_member_required
def criar_quiz(request):
    disciplinas = Disciplina.objects.all()
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        disciplina_id = request.POST.get('disciplina')
        disciplina = get_object_or_404(Disciplina, id=disciplina_id)
        
        # Cria o Quiz
        novo_quiz = Atividade.objects.create(
            titulo=titulo,
            disciplina=disciplina,
            tipo='quiz'
        )
        # Redireciona para a página de adicionar perguntas passando o ID do quiz
        return redirect('professor:adicionar_pergunta', atividade_id=novo_quiz.id)

    return render(request, 'professor/criar_quiz.html', {'disciplinas': disciplinas})

@staff_member_required
def adicionar_pergunta(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    perguntas = atividade.perguntas.all() # Para listar as que já foram criadas

    if request.method == "POST":
        texto = request.POST.get('texto')
        opção_a = request.POST.get('opcao_a')
        opção_b = request.POST.get('opcao_b')
        opção_c = request.POST.get('opcao_c')
        opção_d = request.POST.get('opcao_d')
        correta = request.POST.get('correta') # Pegará o valor de um 'select' ou 'radio'

        Pergunta.objects.create(
            atividade=atividade,
            texto=texto,
            opcao_a=opção_a,
            opcao_b=opção_b,
            opcao_c=opção_c,
            opcao_d=opção_d,
            resposta_correta=correta
        )
        return redirect('professor:adicionar_pergunta', atividade_id=atividade.id)

    return render(request, 'professor/adicionar_pergunta.html', {
        'atividade': atividade,
        'perguntas': perguntas
    })

@staff_member_required
def criar_material(request):
    disciplinas = Disciplina.objects.all()
    
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        disciplina_id = request.POST.get('disciplina')
        descricao = request.POST.get('descricao')
        link_video = request.POST.get('link_video')
        arquivo = request.FILES.get('arquivo') # Para arquivos, usamos request.FILES
        
        disciplina = get_object_or_404(Disciplina, id=disciplina_id)
        
        Atividade.objects.create(
            titulo=titulo,
            disciplina=disciplina,
            descricao=descricao,
            tipo='material', # Forçamos o tipo material
            link_video=link_video,
            arquivo=arquivo
        )
        return redirect('professor:dashboard')

    return render(request, 'professor/criar_material.html', {'disciplinas': disciplinas})
@staff_member_required
def criar_quiz(request):
    disciplinas = Disciplina.objects.all()
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        disciplina_id = request.POST.get('disciplina')
        disciplina = get_object_or_404(Disciplina, id=disciplina_id)

        # Cria o Quiz
        novo_quiz = Atividade.objects.create(
            titulo=titulo,
            disciplina=disciplina,
            tipo='quiz'
        )
        # ✅ Redireciona para a página de adicionar perguntas passando o ID do quiz
        return redirect('professor:adicionar_pergunta', atividade_id=novo_quiz.id)

    return render(request, 'professor/criar_quiz.html', {'disciplinas': disciplinas})

@staff_member_required
def dashboard_professor(request):
    desempenho_recente = Historico.objects.all().select_related('aluno', 'atividade').order_by('-data_conclusao')[:10]
    disciplinas = Disciplina.objects.all()
    total_atividades_concluidas = Historico.objects.count()

    # 🔹 Busca todos os quizzes criados
    quizzes = Atividade.objects.filter(tipo='quiz').select_related('disciplina').order_by('-id')

    return render(request, 'professor/dashboard.html', {
        'desempenho': desempenho_recente,
        'disciplinas': disciplinas,
        'total_concluidas': total_atividades_concluidas,
        'quizzes': quizzes
    })
@staff_member_required
def relatorio_disciplina(request, disciplina_id):
    """
    Página detalhada: mostra a nota de todos os alunos 
    em uma disciplina específica.
    """
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    
    # Filtra o histórico: apenas atividades que pertencem a esta disciplina
    notas_turma = Historico.objects.filter(
        atividade__disciplina=disciplina
    ).select_related('aluno', 'atividade').order_by('aluno__username', '-data_conclusao')

    return render(request, 'professor/relatorio_disciplina.html', {
        'disciplina': disciplina,
        'notas_turma': notas_turma
    })

def aguardando_aprovacao(request):
    return render(request, "professor/aguardando_aprovacao.html")




