from rest_framework import serializers
from .models import Lead,Project


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
