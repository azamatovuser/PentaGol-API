from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer


class ArticleAllListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleLastListAPIView(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer


class ArticleLastFourListAPIView(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-id')[:4]
    serializer_class = ArticleSerializer


class ArticleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer