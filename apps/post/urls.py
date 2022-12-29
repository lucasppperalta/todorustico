from django.urls import path
from . import views
app_name = 'apps.post'

urlpatterns = [
    path('addPost/', views.AddPost.as_view()),
    path('listarPost/', views.mostrarPost.as_view()),
    path('listarPost2/', views.listarPost),
    path('listarCategoria/<str:categoria>', views.ListarPostPorCategoria, name='listarCategoria'),
]