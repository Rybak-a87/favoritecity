from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from favoritecity.ads import choises as mch


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_upl(self):
        # return reverse("company", kwargs={"pk": self.id})
        return f"/category/{self.slug}"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Utils(models.Model):
    name = models.CharField(max_length=100, verbose_name="Удобства", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Удобство"
        verbose_name_plural = "Удобства"


class Advent(models.Model):
    title = models.CharField(max_length=255, verbose_name="")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)   # TODO?
    district = models.PositiveSmallIntegerField(verbose_name="Район", choices=mch.DISTRICT_CHOICE)   # TODO?
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    utils = models.ManyToManyField(Utils, verbose_name="Удобства", blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    price_per = models.PositiveSmallIntegerField(verbose_name="Цена за", choices=mch.PRICE_PER_CHOICE)
    price = models.DecimalField(verbose_name="Цена (грн.)", max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.title} | {self.user.username} | {self.price}"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
