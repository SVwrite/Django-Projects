from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Advance Options', {
                'classes': ('wide', 'extrapretty'),
                'fields': ('role', 'team')
            }
        ),
    )


admin.site.register(User, CustomUserAdmin)
