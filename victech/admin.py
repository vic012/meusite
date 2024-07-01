from django.urls import reverse
from django.contrib import admin
from django.utils.html import mark_safe
from .models import Postagem, Category, Department, Ideias, ReportUserBlog
from .form import PostagemForm


admin.site.register(Category)

class DepartmentAdmin(admin.ModelAdmin):
	filter_horizontal = ("category",)

admin.site.register(Department, DepartmentAdmin)

class PostagemAdmin(admin.ModelAdmin):
	form = PostagemForm
	filter_horizontal = ("category",)
	list_editable = ("ativo", "data_criacao", "data_publicacao")

	list_display = (
	    "titulo",
	    "ativo",
	    "data_criacao",
	    "data_publicacao",
	    "get_link"
	)

	def get_link(self, obj):
	    url = reverse("post_detalhe", args=[obj.slug])
	    link = f"<a href='{url}' target='_blank'>Acessar post</a>"
	    return mark_safe(link)

	get_link.short_description = "Ação"

	class Media:
	    js = ("//code.jquery.com/jquery-3.7.0.min.js",
              "js/post_edit_slug_title.js",)

admin.site.register(Postagem, PostagemAdmin)

admin.site.register(Ideias)

class ReportUserBlogAdmin(admin.ModelAdmin):
	list_display = (
		"address",
		"number_of_requests",
		"last_path",
		"user_agent",
		"created_at",
		"last_access_at",
	)

admin.site.register(ReportUserBlog, ReportUserBlogAdmin)
