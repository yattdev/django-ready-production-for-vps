#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from faker import Faker
from blog.models.category_models import Category
from django.core.files.base import ContentFile

# Create fake object
fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    """Factory for category models"""
    class Meta:
        model =  Category
        # Solution for unique contraint field
        django_get_or_create = ('name',)

    name = fake.name()
    image = factory.LazyAttribute(
            lambda _: ContentFile(
                factory.django.ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'category_image.jpg'
            )
        )
    approved = True
