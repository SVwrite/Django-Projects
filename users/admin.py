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
            'User Role',
            {
                'fields':(
                    'is_team_leader',
                    'is_team_member'
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)


