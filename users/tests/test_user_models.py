import os

from django.contrib.auth import get_user_model
from django.test import TestCase

from users.factories import AdminFactory, UserFactory

# Get Custom User
User = get_user_model()


class UserAccountTestCase(TestCase):
    """ TestCase for UserAccount models"""
    def setUp(self):
        self.user = UserFactory()
        self.admin = AdminFactory()

    def test_if_users_created(self):
        self.assertEqual(User.objects.count(), 2)

    def test_user_content(self):
        user = User.objects.get(id=self.user.id)

        self.assertEqual(f'{user.first_name}', f'{self.user.first_name}')
        self.assertEqual(f'{user.last_name}', f'{self.user.last_name}')
        self.assertEqual(f'{user.password}', f'{self.user.password}')
        self.assertEqual(f'{user.username}', f'{self.user.username}')
        self.assertEqual(f'{user.email}', f'{self.user.email}')

    def test_superuser_content(self):
        superuser = User.objects.get(id=self.admin.id)

        self.assertEqual(f'{superuser.first_name}', f'{self.admin.first_name}')
        self.assertEqual(f'{superuser.last_name}', f'{self.admin.last_name}')
        self.assertEqual(f'{superuser.password}', f'{self.admin.password}')
        self.assertEqual(f'{superuser.username}', f'{self.admin.username}')
        self.assertEqual(f'{superuser.email}', f'{self.admin.email}')
