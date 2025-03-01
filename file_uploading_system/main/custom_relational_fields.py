from rest_framework.serializers import RelatedField, DateField
from datetime import date


class CustomUserPhoneField(RelatedField):
    def to_representation(self, value):
        return f'{value.phone_number} - {value.first_name} {value.last_name}'

class CustomDateField(DateField):
    def to_representation(self, value):
        return date.strftime(value, '%Y-%m-%d')
