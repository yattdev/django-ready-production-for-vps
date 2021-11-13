# Third party imports.
from rest_framework import serializers

# Local application imports
from blog.models.article_models import Article


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.name")
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'title',
            'author',
            'image',
            'image_credit',
            'body',
            'date_published',
            'date_updated',
            'read_time',
            'slug',
        )
