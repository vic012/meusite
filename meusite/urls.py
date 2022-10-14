from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
	path('', views.home.as_view(), name = 'home'),
	path('cnpj', views.cnpj, name = 'cnpj'),
	path('dados-recebidos', views.api, name = 'api'),
	path('cep', views.cep, name = 'cep'),
	path('dados-recebidos-cep', views.api_cep, name = 'api'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)