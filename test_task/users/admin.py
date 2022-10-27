from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AppUser
from .forms import AppUserCreationForm, AppUserChangeForm


class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = ["username", "email", ]
    search_fields = ('username', "email",)


admin.site.register(AppUser, AppUserAdmin)
