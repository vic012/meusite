from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Postagem
from .form import PostagemForm
import json

# Create your views here.
def home(request):
	if (request.method == 'GET'):
		if request.user.is_authenticated:
			postagens = Postagem.objects.filter(data_criacao__lte=timezone.now()).order_by('-data_criacao')
		else:
			postagens = Postagem.objects.filter(ativo=True, data_criacao__lte=timezone.now()).order_by('-data_criacao')
		paginacao = Paginator(postagens, 10) # Mostra x posts por página
		usuario = str(request.user)

		# Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
		try:
			page = int(request.GET.get('page', '1'))
		except ValueError:
			page = 1

		# Se o page request (9999) está fora da lista, mostre a última página.
		try:
			post = paginacao.page(page)
		except (EmptyPage, InvalidPage):
			post = paginacao.page(paginacao.num_pages)

		return render(request, 'base.html', {'post': post, 'usuario':usuario})
	else:
		postagens = Postagem.objects.filter(titulo__icontains=request.POST.get('busca'))

		if (len(postagens) >= 1):
			erro = False
			paginacao = Paginator(postagens, 10) # Mostra x posts por página
			usuario = str(request.user)

			# Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
			try:
				page = int(request.GET.get('page', '1'))
			except ValueError:
				page = 1

			# Se o page request (9999) está fora da lista, mostre a última página.
			try:
				post = paginacao.page(page)
			except (EmptyPage, InvalidPage):
				post = paginacao.page(paginacao.num_pages)

			return render(request, 'base.html', {'post': post, 'usuario':usuario, 'erro': erro})
		else:
			erro = True
			mensagem = f"Infelizmente não consegui encontrar nenhum resultado para o termo: {request.POST.get('busca')}"
			postagens = Postagem.objects.filter(data_criacao__lte=timezone.now()).order_by('-data_criacao')
			paginacao = Paginator(postagens, 10) # Mostra x posts por página
			usuario = str(request.user)

			# Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
			try:
				page = int(request.GET.get('page', '1'))
			except ValueError:
				page = 1

			# Se o page request (9999) está fora da lista, mostre a última página.
			try:
				post = paginacao.page(page)
			except (EmptyPage, InvalidPage):
				post = paginacao.page(paginacao.num_pages)

			return render(request, 'base.html', {'post': post, 'usuario':usuario, 'erro': erro, 'mensagem': mensagem})

def post_detalhe(request, slug):
	post_descricao = get_object_or_404(Postagem, slug=slug)
	table_content = json.loads(post_descricao.table_content) if post_descricao.table_content else {}
	#dados_post = post_descricao.texto.split("\r\n\r\n")
	usuario = str(request.user)
	return render(request, 'post_detalhe.html', {
		'table_content': table_content,
		'post_descricao': post_descricao,
		'dados_post': post_descricao.texto,
		'usuario': usuario
	})

def post_edit(request, slug):
	if (str(request.user) != 'AnonymousUser'):
		postagem = get_object_or_404(Postagem, slug=slug)
		if request.method == "POST":
			formulario = PostagemForm(request.POST, instance=postagem)
			if formulario.is_valid():
				postagem = formulario.save(commit=True)
				return redirect('post_detalhe', slug=postagem.slug)
		else:
			if postagem.table_content:
				table_content = json.loads(postagem.table_content)
				title_content = [content["title"] for content in table_content["content"]]
				title_content = ''.join(title_content)
				css_title_content = [content["css"] for content in table_content["content"]]
				css_title_content = ''.join(css_title_content)
				table_content = {
					'title_content': title_content,
					'css_title_content': css_title_content
				}
			formulario = PostagemForm(initial=table_content, instance=postagem)
	else:
		return redirect('home')

	return render(request, 'novo_post.html', {'formulario': formulario})

#Praticando class based views
#Essa clase fará a edição dos novos posts
class NovoPost(ListView):
	model = Postagem

	def get(self, request):
		formulario = PostagemForm()
		return render(request, 'novo_post.html', {'formulario': formulario})

	def post(self, request):
		if (str(request.user) != 'AnonymousUser'):
			formulario = PostagemForm(request.POST)
			if formulario.is_valid():
				postagem = formulario.save(commit=True)
				return redirect('post_detalhe', slug=postagem.slug)
		else:
			return redirect('home')

		return render(request, 'novo_post.html', {'formulario': formulario})