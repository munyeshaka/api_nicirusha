from django.urls import re_path, path, include
from rest_framework import routers

from .import views

app_name = 'api'


router_api = routers.DefaultRouter()
router_api.register(r'articles', views.ArticleViewSet, basename="articles")
router_api.register(r'last-4-articles', views.Last_4_ArticleViewSet, basename="last-4-articles")

router_api.register(r'autors', views.AutorViewSet, basename="autors")
router_api.register(r'categories', views.CategoryViewSet, basename="categories")

router_api.register(r'autor-latestArticle', views.AutorLatestArticleViewSet, basename="autor-latestArticle")
router_api.register(r'categorie-latestArticle', views.CategoryLatestArticleViewSet, basename="categorie-latestArticle")


urlpatterns = [
    re_path(r'^$', views.home),

    path('api/', include(router_api.urls)),



]