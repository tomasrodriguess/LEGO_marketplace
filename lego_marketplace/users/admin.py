from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

# Register your custom User model using the built-in UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Optional: You can customize how the fields are displayed in the admin interface
    list_display = ('username', 'email', 'is_staff', 'is_superuser','is_moderator')
    search_fields = ('email', 'username')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_moderator', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
