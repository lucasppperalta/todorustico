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

class mostrarPost(ListView):
    model = Post
    template_name = 'post/listarPost.html'

def listarPost(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, 'post/ListarPost2.html', context)

def ListarPostPorCategoria(request, categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)

    post = Post.objects.filter(categoria = categoria2[0].id)
    context = { 
		'post': post,
    }
    return render(request,'post/listarPost2', context)