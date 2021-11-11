from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status, response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.middleware import csrf
from django.http import JsonResponse
from .permissions import IsAuthorOrReadOnly
from itertools import chain
from django.contrib.auth import get_user_model


#  Return CSRF token
def get_csrf_token(request):
    token = csrf.get_token(request)

    return JsonResponse({'csrf_token': token})
