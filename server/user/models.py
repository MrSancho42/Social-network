from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class _UserManager(BaseUserManager):
    def create_user(self, login, username, password, **other_fields):
        if not login:
            raise ValueError('User must have a login')
        if not username:
            raise ValueError('User must have a username')
        if not password:
            raise ValueError('User must have a password')

        user = self.model(login=login, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, login, username, password, **other_fields):
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)

        return self.create_user(login, username, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username     = models.CharField(max_length=150)
    login        = models.CharField(max_length=32, unique=True)
    date_joined  = models.DateTimeField(default=timezone.now)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin     = models.BooleanField(default=False)
    last_activity = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['username', 'password']

    objects = _UserManager()

    def __str__(self):
        return self.login

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    class Meta:
        db_table = 'user'
