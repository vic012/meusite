from django.contrib.sitemaps import Sitemap
from .models import Postagem
from django.urls import reverse


class PostagemSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.9
	protocol = 'https'

	def items(self):
		return Postagem.objects.filter(ativo=True)

	def lastmod(self, obj):
		return obj.data_publicacao

	def location(self, obj):
		return '/blog/post/%s' % (obj.slug)


class StaticSitemap(Sitemap):
	changefreq = "yearly"
	priority = 0.8
	protocol = 'https'

	def items(self):
		return ["my_site:home", "my_site:cnpj", "my_site:cep"]

	def location(self, item):
		return reverse(item)
