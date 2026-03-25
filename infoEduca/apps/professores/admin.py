from django.contrib import admin
from django.utils.html import format_html
from apps.professores.models import Professor

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    # Exibir foto na lista
    def exibir_foto(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover;" />',
                obj.foto.url
            )
        return "Sem foto"
    
    exibir_foto.short_description = 'Foto'

    # Colunas visíveis no admin
    list_display = ('exibir_foto', 'nome', 'especialidade', 'aprovado')
    list_filter = ('aprovado', 'especialidade')
    search_fields = ('nome', 'especialidade')

    # 🔹 Ações em lote
    actions = ['aprovar_professores', 'reprovar_professores']

    def aprovar_professores(self, request, queryset):
        queryset.update(aprovado=True)
        self.message_user(request, "Professores aprovados com sucesso.")

    def reprovar_professores(self, request, queryset):
        queryset.update(aprovado=False)
        self.message_user(request, "Professores reprovados com sucesso.")

    aprovar_professores.short_description = "Aprovar professores selecionados"
    reprovar_professores.short_description = "Reprovar professores selecionados"