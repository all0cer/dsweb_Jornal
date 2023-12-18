from django.urls import path

from . import views

app_name = 'jornal'  #É usado para identificar as URLS pelos nomes invés de toda URL ex: 'jorna:index'
urlpatterns = [
        path('index/', views.IndexView.as_view(), name='index'),
        path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
        path('login/', views.LoginView.as_view(), name='login'),
        path('noticia/<int:pk>/', views.NoticiaDetailView.as_view(), name='noticia_detail'),
        path('logout/', views.LogoutView(), name='logout'),
]