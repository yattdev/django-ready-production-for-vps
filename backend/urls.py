"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

schemas_view = get_schema_view(
    openapi.Info(
        title="RESTFULL API FOR PERSONNAL BLOG APPLICATION",
        description="API MADE WITH\
        DJANGO-POSTGRES-GUNICORN-NGINX-DOCKER",
        default_version="v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alassane@yatt.tech"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin241997/', admin.site.urls),
    path('blog', include('blog.urls')),
    path('api/v1/', include('api.urls')),
    # swagger logout url
    path('accounts/logout/',
         RedirectView.as_view(url=reverse_lazy('blog:logout'))),
    path('accounts/login/',
         RedirectView.as_view(url=reverse_lazy('blog:login'))),
    path('', RedirectView.as_view(url=reverse_lazy('openapi-schemas'))),
    path('api/v1/docs/',
         schemas_view.with_ui('swagger', cache_timeout=0),
         name="openapi-schemas"),

    # CKEditor path
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Url for password reset.
    path('account/password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html'),
         name='password_reset'),

    # Url for successful password reset.
    path('account/password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    # Url for successful password reset confirm.
    path('account/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),

    # Url for password reset done.
    path('account/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
]

# enables django to know location of static and media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
