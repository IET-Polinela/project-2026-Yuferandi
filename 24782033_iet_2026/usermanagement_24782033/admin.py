from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Role Info", {
            "fields": ("is_admin", "is_member")
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)