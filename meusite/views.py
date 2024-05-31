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
        list_courses = Courses.objects.order_by('-date').values(
            "institution", "date", "course"
        )
        context['courses'] = list_courses
        return context


def cnpj(request):
	return render(request, 'indexCnpj.html')

def cep(request):
	return render(request, 'indexCep.html')

def api(request):
	cnpj = request.GET.get('cnpj')
	api = api_cnpj.CNPJ(cnpj)
	data_response = api.consultar_cnpj()

	if data_response.get("content"):
	    contexto = {}
	    contexto['resultado'] = data_response.get("content")
	    return render(request, 'form.html', contexto)

	contexto = {}
	contexto['resultado'] = data_response.get(
	    "message",
	    "Erro ao consultar o CNPJ"
	) or "Erro ao consultar o CNPJ"

	return render(request, 'indexCnpj.html', contexto)

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

			return render(request, 'indexCep.html', contexto)
