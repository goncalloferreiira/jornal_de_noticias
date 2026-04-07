from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticia/<int:id>/', views.detalhe, name='detalhe'),
]