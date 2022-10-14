from django.contrib import admin
from .models import Projects, Courses

# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):

	list_display = (
		"title",
		"date",
		"link_project",
	)

admin.site.register(Projects, ProjectsAdmin)

class CoursesAdmin(admin.ModelAdmin):

	list_display = (
		"course",
		"institution",
		"date",
	)

admin.site.register(Courses, CoursesAdmin)