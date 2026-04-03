from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>O Jornal de Notícias está online.</h1>")