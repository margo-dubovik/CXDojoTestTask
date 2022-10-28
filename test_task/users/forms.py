from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms

from .models import AppUser


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ("username", "email",)


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = ("username", "email",)


class CollectInfoForm(forms.Form):
    csv_file = forms.FileField(required=True)
    xml_file = forms.FileField(required=True)

