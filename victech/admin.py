from django.contrib import admin
from .models import Postagem, Category, Department
from .form import PostagemForm


admin.site.register(Category)

class DepartmentAdmin(admin.ModelAdmin):
	filter_horizontal = ("category",)

admin.site.register(Department, DepartmentAdmin)

class PostagemAdmin(admin.ModelAdmin):
	form = PostagemForm
	filter_horizontal = ("category",)

admin.site.register(Postagem, PostagemAdmin)