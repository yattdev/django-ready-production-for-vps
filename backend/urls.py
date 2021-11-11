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
from django.urls import reverse
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schemas_view = get_schema_view(
    openapi.Info(
        title="Gestion de pochette d'albums API",
        description="A simple API for crud albums pochette",
        default_version="v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="yattdeveloper@gmail"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('openapi-schemas'))),
    path('api/v1/', include('api.urls')),
    # swagger logout url
    path('accounts/logout/', RedirectView.as_view(url=reverse_lazy('logout'))),
    path('accounts/login/', RedirectView.as_view(url=reverse_lazy('login'))),

    path('api/v1/docs', schemas_view.with_ui(
        'swagger', cache_timeout=0
    ), name="openapi-schemas")
]

# enables django to know location of static and media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
