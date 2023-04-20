from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *



class OurHome(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['/'] #, '/about/', '/contact/']

    def location(self, item):
        return item

        

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        # Return a QuerySet of articles you want to include in the sitemap
        return Article.objects.all()

    #Define the `location` method to return the URL for each item in the sitemap
    def location(self, obj):
        # Return the URL for each article in the sitemap
        return reverse('article_detail', args=[obj.slug])
    
    
class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        # Return a QuerySet of Categorys you want to include in the sitemap
        return Category.objects.all()

    #Define the `location` method to return the URL for each item in the sitemap
    def location(self, obj):
        # Return the URL for each Category in the sitemap
        return reverse('category_detail', args=[obj.id])
    
        



