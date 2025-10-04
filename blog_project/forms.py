from django import forms
from admin_app.models import Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Este formulário é usado para criar ou editar notícias, permitindo que o usuário insira título, conteúdo e uma imagem de capa.
class NoticiaForm(forms.ModelForm):
    conteudo = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Digite o conteúdo'}), required=False)

    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo', 'imagem_capa']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título'}),
            'imagem_capa': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }

# Este formulário é usado para criar uma nova conta de usuário, incluindo campos para nome, sobrenome, email e senha.
class CreateAccontForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')