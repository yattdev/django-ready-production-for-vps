#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from faker import Faker
from django.contrib.auth import get_user_model

# Create object faker
fake = Faker()

# Get Custom user as User models
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    username = fake.name()
    password = fake.password()
    email = fake.email()
    admin = False


# Another, different, factory for the same object
class AdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    username = fake.name()
    password = fake.password()
    email = fake.email()
    admin = True
