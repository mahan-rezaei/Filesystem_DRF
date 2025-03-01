from django.contrib import admin
from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'upload_date')
    search_fields = ('uer__phone_number', 'file')
