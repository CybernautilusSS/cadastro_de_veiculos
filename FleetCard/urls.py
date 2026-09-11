from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contatos/', views.contatos, name='contatos'),
    path('pagina_veiculos/', views.pagina_veiculos, name='pagina_veiculos'),
]