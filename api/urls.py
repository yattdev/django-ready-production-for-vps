#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include
from .views.utils_view import get_csrf_token
from .views.article_views import CategoryArticleList, ArticleViewSet
from .views.category_views import CategoryViewSet

from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('get-token/', get_csrf_token, name="get-token"),  # to get csrf_token
    # third party apps urls
    path("auth", include("rest_framework.urls")),
    path('auth', include('djoser.urls'), name="auth"),
    path('auth', include('djoser.urls.jwt')),
    path('auth', include('djoser.urls.authtoken'), name="auth_token"),
]

# ---------------
# Blog endpoints

router = SimpleRouter()

# Article List/Details endpoint by viewsets
router.register('articles', ArticleViewSet, basename="articles")

# Category List/Details endpoint by viewsets
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns += [
    path('<str:category_name>/', CategoryArticleList.as_view()),
] + router.urls
