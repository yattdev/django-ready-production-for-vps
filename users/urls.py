#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from users.views.account.login_view import UserLoginView
from users.views.account.logout_view import UserLogoutView
from users.views.account.register_view import (
    ActivateView,
    AccountActivationSentView,
    UserRegisterView,
)

urlpatterns = [
    # ACCOUNT URLS #

    # account/login/
    path(route='', view=UserLoginView.as_view(), name='login'),
    path(route='account/login/', view=UserLoginView.as_view(), name='login'),

    # account/login/
    path(route='account/register/',
         view=UserRegisterView.as_view(),
         name='register'),

    # account/logout/
    path(route='account/logout/', view=UserLogoutView.as_view(),
         name='logout'),
    path(route='account_activation_sent/',
         view=AccountActivationSentView.as_view(),
         name='account_activation_sent'),
    path(route='activate/<uidb64>/<token>/',
         view=ActivateView.as_view(),
         name='activate'),
]
