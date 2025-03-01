from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'is_admin', 'is_superuser', 'is_active')
    search_fields = ('phone_number', 'first_name', 'last_name', 'email')
    list_filter = ('is_superuser', 'is_admin', 'is_active')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['superuser_status'].disabled = True
        return form
