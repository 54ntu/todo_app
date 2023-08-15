from rest_framework import serializers
from .models import taskModel

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        fields= "__all__"
        model = taskModel