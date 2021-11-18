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

        # ----- Get saved Category
        cls.cat_saved = Category.objects.get(name=cls.category.name)

    def test_if_category_image_exist(self):
        self.assertTrue(
            os.path.exists(f'{settings.MEDIA_ROOT}' +
                           f'{self.cat_saved.image}'))

    def test_if_category_name_not_empty(self):
        self.assertFalse(self.cat_saved.name == '')

    def test_if_category_returns_the_right_human_readable_representation(self):
        self.assertEqual(self.cat_saved.__str__(), self.cat_saved.name)

    def test_if_category_returns_the_right_slug(self):
        self.assertEqual(self.cat_saved.slug, slugify(self.cat_saved.name))

    def test_category_get_absolute_url(self):
        self.assertEquals(
            self.cat_saved.get_absolute_url(),
            reverse('blog:category_articles',
                    kwargs={'slug': self.cat_saved.slug}))

    def test_if_category_not_approuved(self):
        self.assertFalse(self.cat_saved.approved)

    def test_if_category_image_tag_exist(self):
        self.assertTrue(
            f'{self.cat_saved.image_tag()}',
            f'<img src="/media/{self.cat_saved.image}" \
            width="150" height="80"/>')

    @classmethod
    def tearDownClass(cls):
        # Delete test media directory

        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)

        super().tearDownClass()
