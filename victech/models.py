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
	color = models.CharField(verbose_name="Cor", max_length=256, blank=True, null=True, default="")

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


class Ideias(models.Model):
    titulo = models.CharField(max_length=200, default="Ideia")
    ideias = RichTextField(blank=True, null=True, config_name='special')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Ideia"
        verbose_name_plural = "Ideias"


class ReportUserBlog(models.Model):
	address = models.CharField(verbose_name="Endereço", max_length=200, blank=True, null=True)
	number_of_requests = models.PositiveIntegerField(verbose_name="Número de requisições", blank=True, null=True)
	last_path = models.CharField(verbose_name="Última página visualizada", max_length=200, blank=True, null=True)
	user_agent = models.CharField(verbose_name="Detalhes do acesso", max_length=255, blank=True, null=True)
	created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
	last_access_at = models.DateTimeField(verbose_name="Última visita", auto_now=True)

	def __str__(self):
		return f"{self.address} - {self.number_of_requests}"

	class Meta:
		verbose_name = "Relatório de visitas do Blog"
		verbose_name_plural = "Relatório de visitas do Blog"
		unique_together = ("address",)
