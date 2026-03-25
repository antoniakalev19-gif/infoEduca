from django.contrib import admin
from django.utils.html import format_html # Importante para o botão
from .models import Atividade, Pergunta

class PerguntaInline(admin.StackedInline):
    model = Pergunta
    extra = 1

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    # Adicionamos 'ver_pdf' na lista de exibição
    list_display = ('titulo', 'disciplina', 'tipo', 'ver_pdf')
    list_filter = ('tipo', 'disciplina')
    inlines = [PerguntaInline]
    
    # Função para criar o botão de visualização
    def ver_pdf(self, obj):
        if obj.arquivo:
            return format_html(
                '<a href="{}" target="_blank" style="background-color: #007bff; color: white; padding: 5px 10px; border-radius: 4px; text-decoration: none;">📄 Abrir PDF</a>',
                obj.arquivo.url
            )
        return "Sem arquivo"
    
    ver_pdf.short_description = 'Material' # Nome da coluna no Admin

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('disciplina', 'titulo', 'tipo')
        }),
        ('Material de Estudo', {
            'fields': ('descricao', 'arquivo', 'link_video'),
            'classes': ('collapse',),
        }),
    )