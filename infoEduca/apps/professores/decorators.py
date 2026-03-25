from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

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