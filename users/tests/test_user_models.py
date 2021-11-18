from django.contrib.auth import get_user_model
from django.test import TestCase

from users.factories import AdminFactory, UserFactory

# Get Custom User
User = get_user_model()


class UserAccountTestCase(TestCase):
    """ TestCase for UserAccount models"""
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.admin = AdminFactory()

        # --- Get instance saved from db
        cls.user_saved = User.objects.get(id=cls.user.id)
        cls.superuser_saved = User.objects.get(id=cls.admin.id)

    def test_if_users_created(self):
        self.assertEqual(User.objects.count(), 2)

    # --------------- User TestCase ---------------
    def test_user_if_first_name_saved(self):
        self.assertEqual(f'{self.user_saved.first_name}',
                         f'{self.user.first_name}')

    def test_user_if_last_name_saved(self):
        self.assertEqual(f'{self.user_saved.last_name}',
                         f'{self.user.last_name}')

    def test_user_if_password_saved(self):
        self.assertEqual(f'{self.user_saved.password}',
                         f'{self.user.password}')

    def test_user_if_username_saved(self):
        self.assertEqual(f'{self.user_saved.username}',
                         f'{self.user.username}')

    def test_user_if_email_saved(self):
        self.assertEqual(f'{self.user_saved.email}', f'{self.user.email}')

    # --------------- Superuser TestCase ---------------
    def test_if_superuser_first_name_saved(self):
        self.assertEqual(f'{self.superuser_saved.first_name}',
                         f'{self.admin.first_name}')

    def test_if_superuser_last_name_saved(self):
        self.assertEqual(f'{self.superuser_saved.last_name}',
                         f'{self.admin.last_name}')

    def test_if_superuser_password_name_saved(self):
        self.assertEqual(f'{self.superuser_saved.password}',
                         f'{self.admin.password}')

    def test_if_superuser_username_saved(self):
        self.assertEqual(f'{self.superuser_saved.username}',
                         f'{self.admin.username}')

    def test_if_superuser_email_saved(self):
        self.assertEqual(f'{self.superuser_saved.email}',
                         f'{self.admin.email}')
