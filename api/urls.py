#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include
from .views import get_csrf_token

urlpatterns = [
    path('get-token/', get_csrf_token, name="get-token"),  # to get csrf_token 
    # third party apps urls
    path("auth", include("rest_framework.urls")),
    path('auth', include('djoser.urls'), name="auth"),
    path('auth', include('djoser.urls.jwt')),
    path('auth', include('djoser.urls.authtoken'), name="auth_token"),
]
