from django.urls import path
from . import views
app_name = 'apps.post'

urlpatterns = [
    path('addPost/', views.AddPost.as_view()),
    path('listarPost/', views.mostrarPost.as_view(), name='listarPost'),  
    path('campo/', views.mostrarCampo.as_view(), name='listarPost2'),
    path('noticias/', views.mostrarNoticia.as_view(), name='noticias'),
    
]