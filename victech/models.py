from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField

#-------------------> Tutorial <-------------------#
# https://tutorial.djangogirls.org/pt/django_models/
#-------------------> Tutorial <-------------------#


class Category(models.Model):
	name = models.CharField(verbose_name="Categoria", max_length=256, blank=True, null=True, default="Sem Classificação")
	slug = models.CharField(max_length=200, blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class Department(models.Model):
	name_department = models.CharField(verbose_name="Departamento", max_length=256, blank=True, null=True, default="Sem Classificação")
	category = models.ManyToManyField(Category, verbose_name="Categorias")

	def __str__(self):
		return self.name_department


class Postagem(models.Model):
	titulo = models.CharField(max_length=200)
	descricao = models.CharField(max_length=1024, default= 'Descrição do POST')
	texto = RichTextField(blank=True, null=True, config_name='special')
	data_criacao = models.DateTimeField(default=timezone.now)
	data_publicacao = models.DateTimeField(blank=True, null=True)
	ativo = models.BooleanField(default=True)
	slug = models.CharField(max_length=200, blank=True, null=True)
	table_content = models.JSONField(null=True, blank=True, default=dict)
	category = models.ManyToManyField(Category, verbose_name="Categoria", null=True, blank=True)

	def publish(self):
		self.data_publicacao = timezone.now()
		self.save()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titulo)
		super(Postagem, self).save(*args, **kwargs)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['-data_criacao']

