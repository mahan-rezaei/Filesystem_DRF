from rest_framework import serializers
from .models import File
from .custom_relational_fields import CustomUserPhoneField, CustomDateField
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import json
from django.contrib.auth import get_user_model

User = get_user_model()


def file_size_validator(value):
    if value.size > 20 * 1024 * 1024:
        return serializers.ValidationError('file is to large.')


class FileSerializer(serializers.ModelSerializer):
    user = CustomUserPhoneField(read_only=True)
    upload_date = CustomDateField(read_only=True)

    class Meta:
        model = File
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user
        return super().create(validated_data)

    def validate(self, attrs):
        file = attrs.get('file')
        if not file:
            raise serializers.ValidationError('file is none.')
        file_size_validator(file)
        parser = createParser(file)
        metadata = extractMetadata(parser)

        metadata_dict = {}
        for line in metadata.exportPlaintext():
            key, value = line.split(':', 1)
            metadata_dict[key.strip()] = value.strip()

        metadata_json = json.dumps(metadata_dict)
        attrs['metadata'] = metadata_json
        return attrs
