from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Role, Team
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'team',
        'is_staff',
    ]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

# Register your models here.


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register([Role, Team])
