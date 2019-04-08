from django.forms import ModelForm # importante não esquecer de importar
from .models import *
from django.shortcuts import render

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['autor', 'editora', 'isbn', 'numeroPaginas', 'titulo', 'anoPublicacao', 'emailEditora'] # deve ter o mesmo nome e ordem do model

def livro_list(request, template_name='list.html'):
    livro = Livro.objects.all()
    livros = {'lista': livro}
    return render(request, template_name, livros)
