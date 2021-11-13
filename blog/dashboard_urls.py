# Core Django imports.
from django.urls import path

# Blog application imports.
from blog.views.dashboard.author.dashboard_views import (
    DashboardHomeView,
    ArticleWriteView,
    ArticleUpdateView,
    ArticleDeleteView,
    DashboardArticleDetailView,
    ArticlePublishView,
    AuthorWrittenArticlesView,
    AuthorPublishedArticlesView,
    AuthorDraftedArticlesView,
    AuthorDeletedArticlesView,
)

from blog.views.dashboard.author.author_profile_views import (
    AuthorProfileUpdateView,
    AuthorProfileView,
)

from blog.views.account.register_view import \
    (
      ActivateView,
      AccountActivationSentView,
      UserRegisterView,
    )
from blog.views.account.logout_view import UserLogoutView
from blog.views.account.login_view import UserLoginView

# Specifies the app name for name spacing.
app_name = "blog"

# article/urls.py
urlpatterns = [

    # ACCOUNT URLS #

    # account/login/
    path(route='', view=UserLoginView.as_view(), name='login'),

    # account/login/
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

    # DASHBOARD URLS #

    # /author/dashboard/
    path(route="author/dashboard/home/",
         view=DashboardHomeView.as_view(),
         name="dashboard_home"),

    # author/profile/details
    path(route='author/profile/details/',
         view=AuthorProfileView.as_view(),
         name='author_profile_details'),

    # author/profile/update/
    path(route='author/profile/update/',
         view=AuthorProfileUpdateView.as_view(),
         name='author_profile_update'),

    # me/article/write
    path(route='me/article/write/',
         view=ArticleWriteView.as_view(),
         name="article_write"),

    # me/article/<str:slug>/update/
    path(route='me/article/<str:slug>/update/',
         view=ArticleUpdateView.as_view(),
         name="article_update"),

    # /article/<str:slug>/delete/
    path(route='me/article/<str:slug>/delete/',
         view=ArticleDeleteView.as_view(),
         name="article_delete"),

    # /me/<str:slug>/publish/
    path(route="article/<str:slug>/publish/",
         view=ArticlePublishView.as_view(),
         name="publish_article"),

    # /me/articles/written/
    path(route="me/articles/written/",
         view=AuthorWrittenArticlesView.as_view(),
         name="written_articles"),

    # /me/articles/published/
    path(route="me/articles/published/",
         view=AuthorPublishedArticlesView.as_view(),
         name="published_articles"),

    # /me/articles/drafted/
    path(route="me/articles/drafts/",
         view=AuthorDraftedArticlesView.as_view(),
         name="drafted_articles"),

    # /me/articles/deleted/
    path(route="me/articles/deleted/",
         view=AuthorDeletedArticlesView.as_view(),
         name="deleted_articles"),

    # /me/<str:slug>/
    path(route="me/<str:slug>/",
         view=DashboardArticleDetailView.as_view(),
         name='dashboard_article_detail'),
]
