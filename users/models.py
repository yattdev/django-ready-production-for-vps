from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

USER_ROLES = [('Admin', 'Admin'), ('Staff', 'Staff'),
              ('Utilisateur', 'Utilisateur')]


class UserAccountManager(UserManager):
    """ DOCSTRING:
        Define a custom user manager
    """

    # override create user method to accept email as username
    def create_user(self,
                    username=None,
                    email=None,
                    password=None,
                    **extra_fields):

        return super().create_user(username=username,
                                   email=email,
                                   password=password,
                                   **extra_fields)

    # override createusuperuser method to accept email as username
    def create_superuser(self,
                         username=None,
                         email=None,
                         password=None,
                         **extra_fields):

        return super().create_superuser(username=username,
                                        email=email,
                                        password=password,
                                        **extra_fields)


class UserAccount(AbstractUser):
    """ DOCSTRING:
        define a custom user models
    """
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=40,
                            choices=USER_ROLES,
                            default='Utilisateur')

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'password']

    objects = UserAccountManager()

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.username
