import os
import shutil
# Core Django imports.
from blog.models.author_models import Profile
from django.test import TestCase, override_settings
from django.conf import settings
from users.factories import UserFactory
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
        cls.new_profile = AuthorFactory()

        # Get User from databases
        cls.profile_from_db = Profile.objects.get()

    def test_if_user_profile_returns_the_correct_username(self):
        self.assertEqual(self.profile_from_db.__str__(),
                         f"{self.profile_from_db.user.username}'s Profile")

    def test_if_profile_job_title_saved(self):
        self.assertTrue(self.profile_from_db.job_title)

    def test_if_profile_bio_saved(self):
        self.assertTrue(self.profile_from_db.bio)

    def test_if_profile_address_saved(self):
        self.assertTrue(self.profile_from_db.address)

    def test_if_profile_city_saved(self):
        self.assertTrue(self.profile_from_db.city)

    def test_if_profile_zip_code_saved(self):
        self.assertTrue(self.profile_from_db.zip_code)

    def test_if_profile_image_saved(self):
        self.assertTrue(
            os.path.exists(f'{settings.MEDIA_ROOT}' +
                           f'{self.profile_from_db.profile_image}'))

    def test_if_profile_banner_image_saved(self):
        self.assertTrue(
            os.path.exists(f'{settings.MEDIA_ROOT}' +
                           f'{self.profile_from_db.banner_image}'))

    @classmethod
    def tearDownClass(cls):
        # Delete test media directory
        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)

        super().tearDownClass()
