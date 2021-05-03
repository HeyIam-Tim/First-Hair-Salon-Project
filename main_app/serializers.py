from rest_framework import serializers
from .models import WomanService


class WomanServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomanService
        fields = '__all__'



