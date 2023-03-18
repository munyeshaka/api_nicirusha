from django.contrib import admin
from .models import *
from .admin_actions import export_as_csv_action
from import_export.admin import ImportExportModelAdmin
from .resources import *



admin.site.site_header  =  "NICIRUSHA Blog" 
admin.site.site_title  =  "NICIRUSHA Blog admin site"
admin.site.index_title  =  "NICIRUSHA Blog Admin"


class AdminArticle(ImportExportModelAdmin):
    list_display = ['title', 'intro', 'content', 'photo', 'autor', 'category', 'published', 'edit', 'date', 'slug']
    list_editable = ['intro', 'content', 'photo', 'autor', 'category', 'published', 'edit', 'date', 'slug']
    search_fields = ('title', 'intro', 'content', 'photo', 'autor', 'category', 'published', 'edit', 'date', 'slug',)

    prepopulated_fields = {"slug": ("date","title",)}  # new

    actions = [export_as_csv_action()]
    resource_class = ArticleResource

admin.site.register(Article, AdminArticle)


class AdminAutor(ImportExportModelAdmin):
    list_display = ['fullName', 'phone']
    list_editable = ['phone']
    search_fields = ('fullName', 'phone',)

    actions = [export_as_csv_action()]
    resource_class = AutorResource

admin.site.register(Autor, AdminAutor)



class AdminCategory(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ('name',)

    actions = [export_as_csv_action()]
    resource_class = CategoryResource

admin.site.register(Category, AdminCategory)
