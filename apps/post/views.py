from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Post, Categoria
# Create your views here.

class AddPost(CreateView):
    model = Post
    fields = ['titulo', 'texto', 'categoria', 'imagen']
    template_name ='post/addPost.html'
    success_url = reverse_lazy('index')
############################################################

class mostrarPost(ListView):
    model = Post
    template_name = 'post/listarPost.html'


###########################################################

class mostrarCampo(ListView):
    model = Post
    template_name = 'post/listarPost2.html'

###########################################################

class mostrarNoticia(ListView):
    model = Post
    template_name = 'post/noticias.html'
    



