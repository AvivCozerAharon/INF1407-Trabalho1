from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from admin_app.models import Noticia
from .forms import NoticiaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'home.html', {'noticias': noticias})

def noticia_detalhe(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'noticia_detalhe.html', {'noticia': noticia})

@login_required
def adicionar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoticiaForm()

    return render(request, 'adicionar_noticia.html', {'form': form})

def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'create_account.html', {'form': form})
@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html',{'user': user})  