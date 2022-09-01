from django import forms
from ckeditor.fields import RichTextField
from .models import Postagem

class PostagemForm(forms.ModelForm):
    texto = RichTextField()

    class Meta:
        model = Postagem
        fields = ('ativo', 'titulo', 'descricao', 'texto', 'data_criacao', 'data_publicacao')