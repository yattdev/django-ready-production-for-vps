#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

import factory
from faker import Faker

from blog.models.article_models import Article
from users.factories import UserFactory

from .category_factory import CategoryFactory

# Creat object faker
fake = Faker()


class ArticleFactory(factory.django.DjangoModelFactory):
    """Factory models for blog:article models """
    class Meta:
        model = Article
        # Solution for unique contraint field
        django_get_or_create = ('title', )

    category = factory.SubFactory(CategoryFactory)
    title = factory.LazyFunction(fake.unique.name)
    comments = factory.RelatedFactoryList(
        'blog.factories.comment_factory.CommentFactory',
        'article',
        size=10,
    )
    author = factory.SubFactory(UserFactory)
    image = factory.django.ImageField(width=1024,
                                      height=768,
                                      filename='article_image.jpg')
    image_credit = factory.LazyFunction(fake.unique.name)
    body = fake.unique.paragraph(nb_sentences=100)
    tags = fake.name()
    status = 'PUBLISHED'
    read_time = random.randrange(6)
