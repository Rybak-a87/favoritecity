from django.contrib import admin
from favoritecity.ads.models import Ad, Category, Comfort


admin.site.register(Comfort)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name"]
