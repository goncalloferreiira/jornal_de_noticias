from django.shortcuts import render
from .models import Artigo # Importa os teus modelos

def home(request):
    # Vai buscar todos os artigos da base de dados
    artigos = Artigo.objects.all().order_by('-data_publicacao') 
    return render(request, 'jornal/home.html', {'artigos': artigos})