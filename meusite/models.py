from django.db import models

# Create your models here.

class Projects(models.Model):

	title = models.CharField("Titulo do projeto", max_length=255)
	image = models.ImageField(upload_to ='projects/')
	description = models.CharField("Descrição do projeto", max_length=255)
	link_project = models.CharField("Link do projeto", max_length=255, blank=True, null=True)
	date = models.DateField()

	def __str__(self):
		return self.title

	class Meta:
	    verbose_name = "Projeto"
	    verbose_name_plural = "Projetos"

class Courses(models.Model):

    institution = models.CharField("Instituição", max_length=255)
    course = models.CharField("Curso", max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.course

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
