from django.shortcuts import render, get_object_or_404
from .models import Artigo

def home(request):
    artigos = Artigo.objects.all().order_by('-data_publicacao') 
    return render(request, 'jornal/home.html', {'artigos': artigos})

def detalhe(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    return render(request, 'jornal/detalhe.html', {'artigo': artigo})