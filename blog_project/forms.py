from django import forms
from django_ckeditor_5.fields import CKEditor5Field
from admin_app.models import Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoticiaForm(forms.ModelForm):
    from django_ckeditor_5.widgets import CKEditor5Widget
    conteudo = forms.CharField(widget=CKEditor5Widget(config_name = 'default'), required=False)

    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo', 'imagem_capa']
        widgets = {'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título'}),
                               'imagem_capa': forms.FileInput(attrs={'class': 'custom-file-input'}),
}

class CreateAccontForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')