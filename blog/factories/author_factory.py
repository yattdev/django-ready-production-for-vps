#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from faker import Faker
from blog.models.author_models import Profile
from users.factories import UserFactory
from django.core.files.base import ContentFile

# Get object fake
fake = Faker()


class AuthorFactory(factory.django.DjangoModelFactory):
    """
        Factory for blog:Profile models
        is_superuser should be False
    """
    class Meta:
        model = Profile
        # Solution for unique contraint field
        django_get_or_create = ('user', )

    user = factory.SubFactory(UserFactory)
    job_title = fake.profile()['job']
    bio = fake.paragraph()
    address = fake.profile()['address']
    city = fake.profile()['residence']
    zip_code = fake.building_number()
    profile_image = factory.LazyAttribute(lambda _: ContentFile(
        factory.django.ImageField()._make_data({
            'width': 1024,
            'height': 768
        }), 'article_image.jpg'))
    banner_image = factory.LazyAttribute(lambda _: ContentFile(
        factory.django.ImageField()._make_data({
            'width': 200,
            'height': 200
        }), 'banner_image.jpg'))
