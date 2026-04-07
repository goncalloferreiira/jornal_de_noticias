from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario 

def home(request):
    artigos = Artigo.objects.all().order_by('-data_publicacao') 
    return render(request, 'jornal/home.html', {'artigos': artigos})

def detalhe(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    return render(request, 'jornal/detalhe.html', {'artigo': artigo})

def comentarios(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    if request.method == 'POST':
        texto_novo = request.POST.get('texto')
        if texto_novo:
            Comentario.objects.create(artigo=artigo, texto=texto_novo)
            return redirect('comentarios', id=artigo.id)
        
    lista_comentarios = artigo.comentarios.all().order_by('-data_criacao')
        
    return render(request, 'jornal/comentarios.html', {
        'artigo': artigo,
        'comentarios': lista_comentarios
    })