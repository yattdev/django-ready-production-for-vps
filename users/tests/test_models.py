from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy
from rest_framework import status
from django.test import Client
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()  # Get user models


class UserAccountTestCase(TestCase):
    """ TestCase for UserAccount models"""
    @classmethod
    def setUpTestData(cls):
        # Create test user
        cls.user_test = User.objects.create(
            email='user_test@gmail.com',
            password=make_password('test_user123'),
        )
        cls.user_test.save()

        cls.user_test_authtoken = ''  # Update when login user_test

        # Create super user
        cls.test_admin = User.objects.create_superuser(
            email='admin@gmail.com', password='test_admin123')
        cls.test_admin.save()

    @classmethod
    def setUp(cls):
        #  API Client
        cls.client = APIClient()

    def login(self):
        response = self.client.post(reverse_lazy('jwt-create'), {
            'email': 'user_test@gmail.com',
            'password': 'test_user123',
        })
        self.user_test_authtoken = response.json()['access']

    def test_create_user(self):
        user = User.objects.get(email="user_test@gmail.com")
        self.assertEqual(f'{user.email}', f'{self.user_test.email}')
        self.assertTrue(user.check_password('test_user123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superUser = User.objects.get(email='admin@gmail.com')
        self.assertTrue(superUser.check_password('test_admin123'))
        self.assertTrue(superUser.is_superuser)
        self.assertTrue(superUser.is_active)
        self.assertTrue(superUser.is_staff)

    def test_signup_user(self):
        response = self.client.post(reverse_lazy('useraccount-list'), {
            'email': 'yatt@gmail.com',
            'password': 'testpassword_123',
        })

        # Check status response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)
        #  self.client.get(reverse_lazy('logout'))

    def test_login_user(self):
        # Test to login user
        response = self.client.post(reverse_lazy('jwt-create'), {
            'email': 'user_test@gmail.com',
            'password': 'test_user123',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authtoken_user(self):
        self.login()  # login user
        # Test to get user details without creadentials
        response = self.client.get(reverse_lazy('useraccount-me'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test to get user details with creadentials
        self.client = Client(HTTP_AUTHORIZATION='Token ' +
                             f'{self.user_test_authtoken}')
        response = self.client.get(reverse_lazy('useraccount-me'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test user details
        data = response.json()
        self.assertEqual(f'{self.user_test.email}', data['email'])
