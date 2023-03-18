from import_export import resources 
from .models import *


class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


