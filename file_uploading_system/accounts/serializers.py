from rest_framework import serializers
from django.contrib.auth import get_user_model
from .custom_relational_fields import CustomDateField
from main.models import File
from main.serializers import FileSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()
    registered_at = CustomDateField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def get_files(self, obj):
        files = File.objects.filter(user=obj)
        ser_data = FileSerializer(instance=files, many=True).data
        return ser_data


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }
