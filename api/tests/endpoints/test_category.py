#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from rest_framework.test import APITestCase
from django.urls import reverse_lazy
from blog.factories.category_factory import CategoryFactory
from rest_framework import status
from api.serializers.category_serializers import CategorySerializer


class CategoryEndpointTestCase(APITestCase):
    """ Endpoint TestCase for Category endpoints """
    @classmethod
    def setUpTestData(cls):
        # Create a bunch of categories
        cls.categories = CategoryFactory.create_batch(random.randrange(7, 15))
        cls.tenth_categorie_id = cls.categories[7].id

    def test_categories_list_endp(self):
        response = self.client.get(reverse_lazy('categories-list'))

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK,
                         msg="categories-list endpoint not work")
        self.assertEqual(len(response.data), len(self.categories))

    def test_categories_detail_endp(self):
        response = self.client.get(
            reverse_lazy('categories-detail',
                         kwargs={'pk': f'{self.tenth_categorie_id}'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test categorie fields
        self.assertEqual(
            len(response.data),
            len(CategorySerializer().get_fields()),
            msg="categories-detail endpoint returned false length of fields")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()  # To roll-back database after TestCase
