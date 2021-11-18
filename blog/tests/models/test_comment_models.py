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

    def test_if_comment_returns_the_right_user(self):
        self.assertEqual(
            self.comment.__str__(),
            f"Comment by {self.comment.name} on {self.comment.article}")

    def test_comment_content(self):
        comment_saved = Comment.objects.get(email=self.comment.email)
        self.assertEqual(f'{comment_saved.comment}', f'{self.comment.comment}')
        self.assertEqual(f'{comment_saved.article.title}',
                         f'{self.comment.article.title}')
        self.assertTrue(comment_saved.approved)

    @classmethod
    def tearDownClass(cls):
        # Delete test media directory

        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)
