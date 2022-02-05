from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    phone = models.CharField(verbose_name="Номер телефона", max_length=16)
    city = models.CharField(verbose_name="Город проживания", max_length=100)

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"
