from slugify import slugify

from django.db import models
from django.contrib.auth import get_user_model


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


class Comfort(models.Model):
    name = models.CharField(max_length=100, verbose_name="Удобство", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Удобство"
        verbose_name_plural = "Удобства"


class Ad(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, related_name="ads")
    comfort = models.ManyToManyField(Comfort, verbose_name="Удобства", related_name="ads")
    description = models.TextField(verbose_name="Описание")
    region = models.CharField(verbose_name="Область", max_length=255)
    city = models.CharField(verbose_name="Город", max_length=255)
    district = models.CharField(verbose_name="Район", max_length=100)
    address = models.CharField(verbose_name="Адрес", max_length=255)
    payment_type = models.PositiveSmallIntegerField(verbose_name="Тип оплаты")
    price = models.DecimalField(verbose_name="Цена", max_digits=6, decimal_places=2)
    active = models.BooleanField(verbose_name="Объявление активно")
    top = models.BooleanField(verbose_name="В топ", default=False)
    create_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    change_date = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    end_date = models.DateTimeField(verbose_name="Дата окончания активности")

    def get_absolute_upl(self):
        return f"/ad/{slugify(self.title)}"

    def __str__(self):
        return f"{self.title} | {self.user.username} | {self.price}"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
