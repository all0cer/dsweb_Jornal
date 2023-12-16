from django.contrib import admin
from .models import Edicao, Noticia, Usuario, Comentario

admin.site.register(Edicao)
admin.site.register(Noticia)
admin.site.register(Usuario)
admin.site.register(Comentario)