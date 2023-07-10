import json
from django import forms
from .models import Postagem
from ckeditor.fields import RichTextField

class PostagemForm(forms.ModelForm):
    texto = RichTextField()
    title_content = forms.CharField(
        label="Títulos do post",
        help_text="<br><b>Para mais de um separe com vírgula</b>",
        widget=forms.Textarea
    )
    css_title_content = forms.CharField(
        label="ID dos títulos",
        help_text="<br><b>Declare respectivamente entre vírgulas conforme o campo Títulos do post</b>",
        widget=forms.Textarea
    )

    class Meta:
        model = Postagem
        fields = (
            'ativo',
            'titulo',
            'descricao',
            'title_content',
            'css_title_content',
            'texto',
            'data_criacao',
            'data_publicacao',
            'slug'
        )

    def clean(self):
        cleaned_data = super().clean()
        title_content = cleaned_data.get("title_content")
        css_title_content = cleaned_data.get("css_title_content")
        if not title_content or not css_title_content:
            raise forms.ValidationError("Informer os títulos e os IDs")

        title_content = title_content.split(",")
        css_title_content = css_title_content.split(",")
        if len(title_content) != len(css_title_content):
            raise forms.ValidationError("Para cada Título insira um ID")
        
        table_content = {"content":[]}
        for title, css in zip(title_content, css_title_content):
            css = css.strip()
            table_content["content"].append({'title': title, 'css': css})
        try:
            cleaned_data["table_content"] = json.dumps(table_content)
        except json.JSONDecodeError:
            raise forms.ValidationError("Insira um JSON válido.")
        return cleaned_data

    def save(self, commit=True):
        self.instance.table_content = self.cleaned_data["table_content"]
        return super().save(commit)
