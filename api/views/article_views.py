# Third-party apps import
from rest_framework.generics import ListAPIView
from rest_framework import viewsets

# Blog app imports
from blog.models.article_models import Article
from ..serializers.article_serializers import ArticleSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.filter(status='PUBLISHED')
    serializer_class = ArticleSerializer


class CategoryArticleList(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category_name = self.kwargs['category_name']
        articles = Article.objects.filter(category__name=category_name,
                                          category__id=category_id,
                                          status='PUBLISHED')

        return articles
