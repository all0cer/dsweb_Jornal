from django.views import View
from django.views import generic
from .models import Noticia, Usuario, User
from django.utils import timezone
from .forms import FormularioCadastro
from django.shortcuts import render, redirect

class IndexView(generic.ListView):
    model = Noticia
    template_name = 'jornal/index.html'
    context_object_name = 'noticias_recentes'

    def get_queryset(self): #Retorna as 9 notícias mais recentes
        return Noticia.objects.filter(
            data_noticia__lte = timezone.now()).order_by('-data_noticia')[:9]

class CadastroView(View):  # Herde da classe View
    template_name = 'jornal/cadastro.html'

    def get(self, request):
        form = FormularioCadastro()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FormularioCadastro(request.POST)
        if form.is_valid():

            novo_usuario = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha'],
            )
            usuario = Usuario(
                user=novo_usuario,
                nome=form.cleaned_data['nome'],
                sobrenome=form.cleaned_data['sobrenome'],
                email=form.cleaned_data['email'],
                senha=form.cleaned_data['senha'],
            )

            usuario.save()
            return redirect('jornal:index')

        return render(request, self.template_name, {'form': form})

