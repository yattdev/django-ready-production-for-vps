import os
import shutil
# Core Django imports.
from blog.models.author_models import Profile
from django.test import TestCase, override_settings
from django.conf import settings

from blog.factories.author_factory import AuthorFactory


@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR,
                                           'media_dir_for_test/'))
class AuthorProfileTestCase(TestCase):
    """
      Class to test the AuthorProfile Model.
    """
    @classmethod
    def setUpTestData(cls):
        """
         Set up all the tests using model AuthorFactory
        """
        cls.user_profile = AuthorFactory()

    def test_if_user_profile_returns_the_correct_username(self):
        self.assertEqual(self.user_profile.__str__(),
                         f"{self.user_profile.user.username}'s Profile")

    def test_if_profile_contents_are_saved(self):
        # Get saved profile
        profile_saved = Profile.objects.get(user=self.user_profile.user)

        # Test profile conents
        self.assertEqual(f'{profile_saved.job_title}',
                         f'{self.user_profile.job_title}')
        self.assertEqual(f'{profile_saved.bio}', f'{self.user_profile.bio}')
        self.assertEqual(f'{profile_saved.address}',
                         f'{self.user_profile.address}')
        self.assertEqual(f'{profile_saved.city}', f'{self.user_profile.city}')
        self.assertEqual(f'{profile_saved.zip_code}',
                         f'{self.user_profile.zip_code}')
        #  TODO: ImageField doesn't saved, test fail with below code
        self.assertTrue(
            os.path.exists(f'{settings.MEDIA_ROOT}' +
                           f'{self.user_profile.profile_image}'))
        self.assertTrue(
            os.path.exists(f'{settings.MEDIA_ROOT}' +
                           f'{self.user_profile.banner_image}'))

    @classmethod
    def tearDownClass(cls):
        # Delete test media directory

        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)
