from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from admin_app.models import Noticia
from .forms import NoticiaForm

def home(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'home.html', {'noticias': noticias})

def noticia_detalhe(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'noticia_detalhe.html', {'noticia': noticia})

def adicionar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    else:
        form = NoticiaForm()

    return render(request, 'adicionar_noticia.html', {'form': form})