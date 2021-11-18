import os
import shutil
# Core Django imports.
from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.text import slugify

from blog.factories.category_factory import CategoryFactory
# Blog application imports.
from blog.models.category_models import Category


@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR,
                                           'media_dir_for_test_category/'))
class CategoryTestCase(TestCase):
    """
      Class to test the category model.
    """
    @classmethod
    def setUpTestData(cls):
        """
          Set up all the tests using CategoryFactory
        """
        cls.category = CategoryFactory()

    def test_if_category_returns_the_right_human_readable_representation(self):
        self.assertEqual(self.category.__str__(), self.category.name)

    def test_if_category_returns_the_right_slug(self):
        self.assertEqual(self.category.slug, slugify(self.category.name))

    def test_category_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('blog:category_articles',
                    kwargs={'slug': self.category.slug}))

    def test_category_contents(self):
        # Get category saved
        cat_saved = Category.objects.get(name=self.category.name)
        self.assertFalse(cat_saved.approved)
        self.assertTrue(
            os.path.exists(f'{settings.MEDIA_ROOT}' + f'{cat_saved.image}'))
        self.assertTrue(
            f'{cat_saved.image_tag()}',
            f'<img src="/media/{cat_saved.image}" width="150" height="80"/>')

    @classmethod
    def tearDownClass(cls):
        # Delete test media directory

        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)
