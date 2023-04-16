
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
# from django.views.generic import TemplateView
from .import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#####  SEO
from django.contrib.sitemaps.views import sitemap
from api.sitemaps import *



router_api = routers.DefaultRouter()
router_api.register(r'articles', views.ArticleViewSet, basename="articles")
router_api.register(r'last-4-articles', views.Last_4_ArticleViewSet, basename="last-4-articles")

router_api.register(r'autors', views.AutorViewSet, basename="autors")
router_api.register(r'categories', views.CategoryViewSet, basename="categories")

router_api.register(r'autor-latestArticle', views.AutorLatestArticleViewSet, basename="autor-latestArticle")
router_api.register(r'categorie-latestArticle', views.CategoryLatestArticleViewSet, basename="categorie-latestArticle")


    #####  for SEO
sitemaps = {
    # 'sitemaps1': YourSitemapClass1,
    'article-detail': ArticleSitemap,
}


urlpatterns = [
    path('alainPro/', admin.site.urls),
    path('api/', include(router_api.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include('api.urls')),

        #####  for 404
    # re_path("^(?!media)(?!admin)(?!api)(?!static).*$", TemplateView.as_view(template_name='green_backend/index.html')),
    
        #####  for SEO
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'), 

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
