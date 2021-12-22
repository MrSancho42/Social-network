from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdminConfig(UserAdmin):
    ordering = ('date_joined', )
    list_display = ('id', 'username', 'login', 'date_joined', 'last_login', 'last_activity')


admin.site.register(User, UserAdminConfig)
