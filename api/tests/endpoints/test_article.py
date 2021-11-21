#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers.article_serializers import ArticleSerializer
from blog.factories.article_factory import ArticleFactory
from blog.models.category_models import Category
from blog.models.article_models import Article


class ArticleEndpointTestCase(APITestCase):
    """Article endpoint test cases"""
    @classmethod
    def setUpTestData(cls):
        # Create 10 articles to databases
        nb_article = random.randrange(3, 10)
        cls.articles = ArticleFactory.create_batch(nb_article)
        cls.third_art_id = cls.articles[2].id

    def test_article_list_endp(self):
        response = self.client.get(reverse_lazy('articles-list'),
                                   format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK,
                         msg='articles-list endpoint not work')
        self.assertEqual(
            len(response.data),
            len(self.articles),
            msg="articles-list endpoint returned false length of articles")

    def test_article_detail_endp(self):
        response = self.client.get(
            reverse_lazy('articles-detail',
                         kwargs={'pk': f'{self.third_art_id}'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test article fields
        self.assertEqual(
            len(response.data),
            len(ArticleSerializer().get_fields()),
            msg="articles-detail endpoint returned false length of fields")

    def test_categorie_articles_endp(self):
        # Get first first_cat from database
        first_cat = Category.objects.first()
        first_cat_articles = Article.objects.filter(
            category__name=first_cat.name)

        response = self.client.get(
            reverse_lazy('categorie-articles',
                         kwargs={
                             'category_id': f'{first_cat.id}',
                             'category_name': f'{first_cat.name}'
                         }))
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK,
                         msg="categorie-articles endpoint not work")

        self.assertEqual(
            len(first_cat_articles),
            len(response.data),
            msg="categorie-articles endpoint returned false length of articles"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()  # To roll-back database after TestCase
