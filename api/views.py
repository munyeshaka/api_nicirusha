from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import *
from django.shortcuts import render


def home(request):
    return render(request, 'api/index.html')


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(published=1, edit=1).order_by('-id')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



######

class AutorLatestArticleViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorLatestArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryLatestArticleViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryLatestArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
