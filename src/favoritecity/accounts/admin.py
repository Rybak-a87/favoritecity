from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2',
                           'first_name', 'last_name'),
                'classes': ('wide',)}),
    )
    list_display = ("__str__", "last_name", "is_active")
