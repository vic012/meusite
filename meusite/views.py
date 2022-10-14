from django.shortcuts import render
from django.views.generic import ListView
from . import api_cnpj
from . import apiCep
from .models import Projects, Courses


class home(ListView):
    #model = Projects
    template_name = "index.html"
    context_object_name = 'projects'

    def get_queryset(self):
        return Projects.objects.order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        context['courses'] = Courses.objects.order_by('-date')
        return context


def cnpj(request):
	return render(request, 'indexCnpj.html')

def cep(request):
	return render(request, 'indexCep.html')

def api(request):
	cnpj = request.GET.get('cnpj')
	api = api_cnpj.CNPJ(cnpj)
	api.consulta()
	if (api.demonstra == 'Por favor, verifique se o número digitado está correto'):
		resultado = {'nome': 'Por favor, verifique se o número digitado está correto'}

		contexto = {}
		contexto['resultado'] = resultado

		return render(request, 'indexCnpj.html', contexto)
	elif (api.demonstra == 'Por favor, Insira um cnpj com 14 dígitos e sem . / ou -'):
		resultado = {'nome': 'Por favor, insira um cnpj com 14 dígitos e sem . / ou -'}

		contexto = {}
		contexto['resultado'] = resultado

		return render(request, 'indexCnpj.html', contexto)
	else:
		resultado = api.demonstra

		contexto = {}
		contexto['resultado'] = resultado

		return render(request, 'form.html', contexto)

def api_cep(request):
	cep = request.GET.get('cep')
	if (len(cep) != 8):
		resultado = {'nome': 'Por favor, insira um CEP com 8 dígitos e sem . / ou -'}
		contexto = {}
		contexto['resultado'] = resultado
		return render(request, 'indexCep.html', contexto)
	else:
		api = apiCep.Cep(cep)
		api.validaCep()
		if (api.resultado != 'CEP inválido'):
			resultado = api.resultado

			contexto = {}
			contexto['resultado'] = resultado
			return render(request, 'formCep.html', contexto)
		else:
			resultado = {'nome': 'O CEP informado é inválido'}

			contexto = {}
			contexto['resultado'] = resultado

			return render(request, 'indexCEP.html', contexto)
