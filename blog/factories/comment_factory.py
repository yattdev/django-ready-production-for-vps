#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from faker import Faker
from blog.models.comment_models import Comment
from .article_factory import ArticleFactory

# Creat fake object
fake = Faker()


class CommentFactory(factory.django.DjangoModelFactory):
    """Factory class for blog:Comment models"""
    class Meta:
        model = Comment
        django_get_or_create = ('article', )

    name = fake.name()
    email = fake.email()
    comment = fake.text()
    article = factory.SubFactory(ArticleFactory)
