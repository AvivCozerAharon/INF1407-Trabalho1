from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from admin_app.models import Noticia
from .forms import NoticiaForm,CreateAccontForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    for n in noticias:
        try:
            user = User.objects.get(id=n.autor_id)
            n.autor_nome = f"{user.first_name} {user.last_name}"
        except User.DoesNotExist:
            n.autor_nome = "Desconhecido"
    return render(request, 'home.html', {'noticias': noticias})

def noticia_detalhe(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'noticia_detalhe.html', {'noticia': noticia})

@login_required
def adicionar_noticia(request):
    if request.method == 'POST':
        user_id = request.user.id
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False) 
            noticia.autor_id = user_id
            noticia.save()
            return redirect('home')
    else:
        form = NoticiaForm()

    return render(request, 'adicionar_noticia.html', {'form': form})

def create_account(request):
    if request.method == 'POST':
        form = CreateAccontForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateAccontForm()
    return render(request, 'create_account.html', {'form': form})
@login_required
def profile(request):
    user = request.user
    noticias = Noticia.objects.filter(autor_id=user.id).order_by('-data_publicacao')

    return render(request, 'profile.html',{'user': user, 'noticias': noticias})  

@login_required
def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    if noticia.autor_id != request.user.id:
        return redirect('home')

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoticiaForm(instance=noticia)

    return render(request, 'editar_noticia.html', {'form': form, 'noticia': noticia})


@login_required
def apagar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk, autor_id=request.user.id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('home')
    return render(request, 'confirmar_delete.html', {'noticia': noticia})