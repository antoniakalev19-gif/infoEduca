from django import forms
from .models import MensagemSuporte

class MensagemSuporteForm(forms.ModelForm):
    class Meta:
        model = MensagemSuporte
        fields = ["nome", "email", "mensagem"]