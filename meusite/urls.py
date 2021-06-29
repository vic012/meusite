from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('cnpj', views.cnpj, name = 'cnpj'),
	path('dados-recebidos', views.api, name = 'api'),
	path('cep', views.cep, name = 'cep'),
	path('dados-recebidos-cep', views.api_cep, name = 'api'),
]