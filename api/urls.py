from django.urls import re_path, path

# #####  SEO
# from django.contrib.sitemaps.views import sitemap
# from api.sitemaps import OurSitemap


from .import views

app_name = 'api'


#     #####  for SEO
# sitemaps = {
#     'api': OurSitemap,
# }

urlpatterns = [
    re_path(r'^$', views.home),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  

]