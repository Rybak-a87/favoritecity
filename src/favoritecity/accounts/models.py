from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone = models.CharField(max_length=16, verbose_name="Номер телефона")

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"
