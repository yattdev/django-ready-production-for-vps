#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from faker import Faker

from blog.models.author_models import Profile
from users.factories import UserFactory

# Get object fake
fake = Faker()


# Return value of given field from person profile
def profile_detail(field):
    return fake.profile()[field]


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
    job_title = factory.LazyAttribute(lambda x: fake.profile()['job'])
    bio = factory.LazyFunction(fake.paragraph)
    address = factory.LazyAttribute(lambda x: fake.profile()['address'])
    city = factory.LazyAttribute(lambda x: fake.profile()['residence'])
    zip_code = factory.LazyFunction(fake.building_number)
    profile_image = factory.django.ImageField(width=400,
                                              height=200,
                                              filename='photo_de_profile.jpg')
    banner_image = factory.django.ImageField(width=800,
                                             height=300,
                                             filename='photo_de_banner.jpg')
