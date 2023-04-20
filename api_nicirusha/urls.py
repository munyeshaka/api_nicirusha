
from django.contrib import admin
from django.urls import re_path, path, include

from django.views.generic import TemplateView
from .import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# #####  SEO
from django.contrib.sitemaps.views import sitemap
from api.sitemaps import *
from api import views





    #####  for SEO
sitemaps = {
    # 'sitemaps1': YourSitemapClass1,
    'home': OurHome,
    'article': ArticleSitemap,
    'categ': CategorySitemap
}


urlpatterns = [
    path('alainPro/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include('api.urls')),

    #####  for 404
    re_path("^(?!media)(?!admin)(?!api)(?!static)(?!sitemap.xml).*$", TemplateView.as_view(template_name='api/index.html')),
    
    ### SEO
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('category/<int:id>/', views.category_detail, name='category_detail'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
