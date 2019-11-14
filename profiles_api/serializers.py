from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializes the demo"""
    name = serializers.CharField(max_length=10)
