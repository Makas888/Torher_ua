from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['username', 'last_name', 'email', 'phone', 'gender']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Додаткова інформація',
            {
                'fields': (
                    'email',
                    'gender',
                    'phone',
                    'groups',
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Додаткова інформація',
            {
                'fields': (
                    'gender',
                    'phone',
                )
            }
        )
    )
