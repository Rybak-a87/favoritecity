from django import forms
from django.contrib.auth.forms import UserCreationForm

from favoritecity.accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user with correct Meta class.
    """
    def __init__(self, *args, **kwargs):
        """
        Pop `request` from method's parameters.

        :param list args: arbitrary argument list
        :param dict kwargs: keyword arguments
        """
        kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.username = user.email

        if commit:
            user.save()
        return user
