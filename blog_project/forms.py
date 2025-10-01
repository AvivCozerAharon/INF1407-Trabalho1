from django import forms
from admin_app.models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo', 'imagem_capa']

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título'}),
            'conteudo': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Digite o conteúdo'}),
        }
