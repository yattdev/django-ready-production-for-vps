# Third-party apps import
from rest_framework import viewsets

# Local application imports
from blog.models.article_models import Category
from ..serializers.category_serializers import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
