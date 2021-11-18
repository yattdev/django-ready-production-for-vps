#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from django.core.files.base import ContentFile
from faker import Faker

from blog.models.category_models import Category

# Create fake object
fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    """Factory for category models"""
    class Meta:
        model = Category
        # Solution for unique contraint field
        django_get_or_create = ('name', )

    name = fake.unique.name()
    image = factory.django.ImageField(width=1024,
                                      height=768,
                                      filename='category_image.jpg')
    approved = False
