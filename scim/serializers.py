from rest_framework import serializers
from .models import ScimApp

class ScimAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScimApp
        fields = '__all__'

