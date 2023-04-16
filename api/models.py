from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify



class Autor(models.Model):
    fullName = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=False, null=True)
    
    def __str__(self):
        return self.fullName



class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = ("Categories")




class Article(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    content = models.TextField()
    photo =  models.ImageField(upload_to='%Y/%m/')
    
    autor =  models.ForeignKey(Autor, related_name="article", default=1, on_delete=models.CASCADE)
    category =  models.ForeignKey(Category, related_name="article", default=1, on_delete=models.CASCADE)

    published = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    date = models.DateField(default=datetime.now())
    updated_at = models.DateField(default=datetime.now())
    slug = models.SlugField(null=False, unique=True)
    ## or slug = AutoSlugField(populate_from=['title'])

    # def __str__(self):
    #     return self.title
    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        # return reverse("article_detail", kwargs={"slug": self.slug})
        return reverse("article-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)