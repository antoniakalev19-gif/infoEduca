from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from apps.disciplinas.models import Disciplina
from apps.atividades.models import Atividade
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import MensagemSuporteForm

def suporte(request):
    if request.method == "POST":
        form = MensagemSuporteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sua mensagem foi enviada! Em breve o suporte entrará em contato.")
            return redirect("suporte")
    else:
        form = MensagemSuporteForm()
    return render(request, "core/suporte.html", {"form": form})



def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {usuario}! Faça login para continuar.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})

def home(request):
    # Pega as 3 últimas disciplinas cadastradas
    disciplinas = Disciplina.objects.all().order_by('-id')[:3]
    # Pega as 5 atividades mais recentes
    atividades_recentes = Atividade.objects.all().order_by('-id')[:5]
    
    context = {
        'disciplinas': disciplinas,
        'atividades_recentes': atividades_recentes,
    }
    return render(request, 'core/home.html', context)
@login_required
def redirecionar_apos_login(request):
    # 1. Verifica se é Admin (Superusuário)
    if request.user.is_superuser:
        return redirect('/admin/')
    
    # 2. Verifica se é Professor (usando o atributo is_staff ou grupo)
    elif request.user.is_staff:
        return redirect('professor:dashboard')
    
    # 3. Se não for nenhum dos dois, é Estudante
    else:
        return redirect('atividades:atividades_home')