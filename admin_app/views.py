from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import NoticiaForm
from .models import Noticia

# Create your views here.

@login_required
def adicionar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.save()
            return redirect('home')
    else:
        form = NoticiaForm()
    return render(request, 'adicionar_noticia.html', {'form': form})

@login_required
def noticia_detalhe(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'noticia_detalhe.html', {'noticia': noticia})
