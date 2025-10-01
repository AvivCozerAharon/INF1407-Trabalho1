from django import forms
from django_ckeditor_5.fields import CKEditor5Field
from admin_app.models import Noticia

class NoticiaForm(forms.ModelForm):
    from django_ckeditor_5.widgets import CKEditor5Widget
    conteudo = forms.CharField(widget=CKEditor5Widget(config_name = 'default'), required=False)

    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo', 'imagem_capa']
        widgets = {'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título'})}