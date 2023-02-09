from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import RegistrarUsuarios
from . import views

app_name="apps.usuario"

urlpatterns = [
    #path('usuario/', views.ListarPost, name="usuario"),
    path('login/',LoginView.as_view(template_name="usuario/login.html"),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('registrar/', views.RegistrarUsuarios.as_view(), name="registrar")
]