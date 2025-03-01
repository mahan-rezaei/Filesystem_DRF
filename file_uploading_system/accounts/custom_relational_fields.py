from rest_framework.serializers import RelatedField, DateField
from datetime import date


class CustomDateField(DateField):
    def to_representation(self, value):
        return date.strftime(value, '%Y-%m-%d')