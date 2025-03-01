from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import os

User = get_user_model()


TEXT_EXTENSIONS = ['txt', 'json', 'xml', 'csv', 'pdf']
IMAGE_EXTENSIONS = ['jpg', 'png', 'gif', 'tiff']


def custom_upload_to(instance, file_name):
    file_extension = file_name.split('.')[-1].lower()
    base_dir = 'files/'
    if file_extension in TEXT_EXTENSIONS:
        upload_path = os.path.join(base_dir, 'text_files', file_name)
    elif file_extension in IMAGE_EXTENSIONS:
        upload_path = os.path.join(base_dir, 'image_files', file_name)
    else:
        raise ValidationError('unsupported file extension.')

    return upload_path


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=custom_upload_to)
    metadata = models.JSONField(blank=True, null=True)

    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.phone_number} - {self.file.name}'

