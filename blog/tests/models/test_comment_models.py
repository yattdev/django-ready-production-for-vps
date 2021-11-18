import os
import shutil

# Core Django imports.
from django.conf import settings
from django.test import TestCase, override_settings

from blog.factories.comment_factory import CommentFactory
# Blog application imports.
from blog.models import Article
from blog.models.comment_models import Comment


@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR,
                                           'media_dir_for_test_comment/'))
class CommentTestCase(TestCase):
    """
      Class to test the Blog model.
    """
    @classmethod
    def setUpTestData(cls):
        """
          Set up all the tests using model_mommy.
        """
        cls.comment = CommentFactory()

        # Get one comment from comment list
        cls.comment_saved = Comment.objects.get()

    def test_if_comment_returns_the_right_user(self):
        self.assertEqual(
            self.comment.__str__(),
            f"Comment by {self.comment.name} on {self.comment.article}")

    def test_if_comment_body_not_empty(self):
        self.assertTrue(f'{self.comment_saved.comment}' != '')

    def test_if_comment_title_not_empty(self):
        self.assertTrue(f'{self.comment_saved.article.title}' != '')

    def test_if_comment_approuve_correctly_saved(self):
        self.assertTrue(self.comment_saved.approved)

    @classmethod
    def tearDownClass(cls):
        # Delete test media directory

        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)
        super().tearDownClass()
