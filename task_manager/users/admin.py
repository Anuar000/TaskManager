from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_staff', 'date_joined']
    search_fields = ['username', 'email']