# Core Django imports.
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Get Custom User as User
User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(verbose_name="Image du profile",
                                      default='profile-pic-default.jpg',
                                      upload_to='profile_pic')
    banner_image = models.ImageField(verbose_name="Image du banner",
                                     default='slider-1.jpg',
                                     upload_to='banner')
    job_title = models.CharField(max_length=100)
    bio = models.CharField(max_length=255,
                           help_text="Short Bio (eg. I love cats and games)")

    address = models.CharField(max_length=100, help_text="Enter Your Address")

    city = models.CharField(max_length=100, help_text="Enter Your City")

    country = models.CharField(max_length=100, help_text="Enter Your Country")

    zip_code = models.CharField(max_length=100,
                                help_text="Enter Your Zip Code")

    twitter_url = models.CharField(
        max_length=250,
        default="#",
        blank=True,
        null=True,
        help_text="Enter # if you don't have an account")
    instagram_url = models.CharField(
        max_length=250,
        default="#",
        blank=True,
        null=True,
        help_text="Enter # if you don't have an account")
    facebook_url = models.CharField(
        max_length=250,
        default="#",
        blank=True,
        null=True,
        help_text="Enter # if you don't have an account")
    github_url = models.CharField(
        max_length=250,
        default="#",
        blank=True,
        null=True,
        help_text="Enter # if you don't have an account")

    email_confirmed = models.BooleanField(default=False)

    created_on = models.DateTimeField(default=timezone.now)

    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
