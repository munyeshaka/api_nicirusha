from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import *


class ArticleSitemap(Sitemap):
    changefreq = 'never' # Set the desired changefreq for your articles

    def items(self):
        # Return a QuerySet of articles you want to include in the sitemap
        return Article.objects.all()

    #Define the `location` method to return the URL for each item in the sitemap
    def location(self, obj):
        # Return the URL for each article in the sitemap
        return reverse('article-detail', args=[obj.id])

    # def location(self, item):
    #     return reverse(item)
    
    def lastmod(self, obj):
        # Return the last modification date of each article (optional)
        return obj.updated_at
                    




