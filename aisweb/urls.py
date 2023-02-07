from django.urls import path
from .views import IndexView

urlpatterns = [
	path('crawler/', IndexView.as_view(), name='aisweb'),
]