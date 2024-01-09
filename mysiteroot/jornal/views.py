from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views import generic
from .models import Noticia, Usuario, User, Comentario, Edicao
from django.utils import timezone
from .forms import FormularioCadastro, FormularioNoticia
from django.shortcuts import render, redirect

class IndexView(generic.ListView):
    model = Edicao
    template_name = 'jornal/index.html'
    context_object_name = 'noticias_recentes'

    def get_queryset(self):
        ultima_edicao =  Edicao.objects.latest('data_edicao')
        return ultima_edicao.noticia_set.all()[0:5]

class CadastroView(View):  # Herde da classe View
    template_name = 'jornal/cadastro.html'

    def get(self, request):
        form = FormularioCadastro()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FormularioCadastro(request.POST)
        if form.is_valid():

            novo_usuario = User.objects.create_user(
                username=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha'],
            )
            usuario = Usuario(
                user=novo_usuario,
                sobrenome=form.cleaned_data['sobrenome'],
            )

            usuario.save()
            return redirect('jornal:index')

        return render(request, self.template_name, {'form': form})

class LoginView(LoginView): # Cria formulário já com authenticate() e get() e post()
    template_name = 'registration/login.html'

def LogoutView(request):
    logout(request)

    return redirect('jornal:index')

class NoticiaDetailView(generic.DetailView):
    model = Noticia
    template_name = "jornal/noticia_detalhe.html"

def ComentarView(request, pk):
    noticia = Noticia.objects.get(pk=pk)

    if request.method == 'POST':
        texto_comentario = request.POST.get('texto_comentario')
        if texto_comentario:
            comentario = Comentario(noticia=noticia, texto_comentario=texto_comentario)
            comentario.save()
    return redirect('jornal:noticia_detalhe', pk=pk)

class ListarEdicoesView(generic.ListView):
    model = Edicao
    template_name = 'jornal/listar_edicoes.html'
    context_object_name = 'edicoes'

class ListarNoticiaPorEdicaoView(View):
    template_name = 'jornal/listar_noticias.html'
    
    def get(self, request, pk):
        edicao = Edicao.objects.get(pk=pk)
        noticias_edicao = edicao.noticia_set.all()
        return render(request, self.template_name , {'noticias_edicao': noticias_edicao})
            
class CadastrarNoticiaView(View):
    template_name = 'jornal/cadastro_noticia.html'

    def get(self, request):
        form = FormularioNoticia()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = FormularioNoticia(request.POST)
        if form.is_valid():
            nova_noticia = Noticia.objects.create(
                edicao=form.cleaned_data['edicao'],
                titulo=form.cleaned_data['titulo'],
                texto_noticia=form.cleaned_data['texto_noticia'],
                data_noticia=form.cleaned_data['data_noticia'],
            )
            nova_noticia.save()
            return redirect('jornal:index')
        return render(request, self.template_name, {'form': form})
        

    