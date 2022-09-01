from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('post/<int:pk>/', views.post_detalhe, name = 'post_detalhe'),
	path('novo_post/', views.NovoPost.as_view(), name= 'novo_post'),
	path('post_edit/<int:pk>/', views.post_edit, name= 'post_edit'),
]