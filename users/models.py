from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField()
    registration_date = models.DateField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    objects = CustomUserManager()
