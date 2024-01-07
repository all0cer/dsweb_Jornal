from django.urls import path

from . import views

app_name = 'jornal'  #É usado para identificar as URLS pelos nomes invés de toda URL ex: 'jorna:index'
urlpatterns = [
        path('index/', views.IndexView.as_view(), name='index'),
        path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
        path('login/', views.LoginView.as_view(), name='login'),
        path('noticia/<int:pk>', views.NoticiaDetailView.as_view(), name='noticia_detalhe'),
        path('logout/', views.LogoutView, name='logout'),
        path('comentar/<int:pk>', views.ComentarView, name='comentar'),
        path('edicoes/', views.ListarEdicoesView.as_view(), name='listar_edicoes'),
        path('noticias/<int:pk>', views.ListarNoticiaPorEdicaoView.as_view(), name='listar_noticias'),
]