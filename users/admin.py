from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model() # Define our custom user

class CustomUserAdmin(UserAdmin):
        model = CustomUser
        list_display = ['email', 'username', 'is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)
