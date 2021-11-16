import os
import shutil
# Core Django imports.
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.text import slugify

from blog.factories.article_factory import ArticleFactory
# Blog application imports.
from blog.models.article_models import Article


@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR,
                                           'media_dir_for_test/'))
class ArticleTestCase(TestCase):
    """
      Class to test the article model.
    """
    @classmethod
    def setUpTestData(cls):
        """
          Set up all the tests using ArticleFactory
        """
        cls.article = ArticleFactory()

    def test_if_article_returns_the_right_human_readable_representation(self):
        self.assertEqual(self.article.__str__(), self.article.title)

    def test_if_article_returns_the_right_slug(self):
        self.assertEqual(self.article.slug, slugify(self.article.title))

    def test_article_get_absolute_url(self):
        self.assertEquals(
            self.article.get_absolute_url(),
            reverse('blog:article_detail',
                    kwargs={
                        'username': self.article.author.username.lower(),
                        'slug': self.article.slug
                    }))

    def test_article_contents(self):
        # Get article saved
        article_saved = Article.objects.get(title=self.article.title)
        self.assertEqual(article_saved.body, self.article.body)
        self.assertEqual(article_saved.image_credit, self.article.image_credit)
        self.assertTrue(article_saved.tags)
        self.assertEqual(article_saved.status, self.article.status)
        self.assertEqual(f'{article_saved.read_time}',
                         f'{self.article.read_time}')
        self.assertTrue(
            os.path.exists(f'{settings.MEDIA_ROOT}' + f'{self.article.image}'))

    @classmethod
    def tearDownClass(cls):
        # Delete test media directory

        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)
