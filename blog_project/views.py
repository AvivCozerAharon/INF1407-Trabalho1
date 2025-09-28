from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from admin_app.models import Noticia

def home(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'home.html', {'noticias': noticias})

def noticia_detalhe(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'noticia_detalhe.html', {'noticia': noticia})