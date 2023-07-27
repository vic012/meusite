from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('<str:category_slug>/', views.home, name = 'home_with_category'),
	path('post/<str:slug>/', views.post_detalhe, name = 'post_detalhe'),
	path('novo_post/', views.NovoPost.as_view(), name= 'novo_post'),
	path('post_edit/<str:slug>/', views.post_edit, name= 'post_edit'),
]