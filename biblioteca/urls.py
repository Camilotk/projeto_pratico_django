from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
        url(r"^listar_livros/", livro_list, name="lista_livros"),
]
