# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        lookup_field = 'slug' ## instead of id
        fields = '__all__'


class AutorSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    def get_articles(self, autor):
        qs = Article.objects.filter(autor=autor).order_by('-date') #autor must be a attr of article model who received foreign key
        serializer = ArticleSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Autor
        fields = ['id', 'fullName', 'phone', 'articles']



class CategorySerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    def get_articles(self, category):
        qs = Article.objects.filter(category=category).order_by('-date') #category must be a attr of article model who received foreign key
        serializer = ArticleSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ['id', 'name', 'articles']



####################


class AutorLatestArticleSerializer(serializers.ModelSerializer):
    latestArticle = serializers.SerializerMethodField()

    def get_latestArticle(self, autor):
        qs = Article.objects.filter(autor=autor).order_by('-date')[0:1] #autor must be a attr of article model who received foreign key
        serializer = ArticleSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Autor
        fields = ['id', 'fullName', 'phone', 'latestArticle']



class CategoryLatestArticleSerializer(serializers.ModelSerializer):
    latestArticle = serializers.SerializerMethodField()

    def get_latestArticle(self, category):
        qs = Article.objects.filter(category=category).order_by('-date')[0:1]  #category must be a attr of article model who received foreign key
        serializer = ArticleSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ['id', 'name', 'latestArticle']

