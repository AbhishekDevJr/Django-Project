from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length = 100, required=True)
    last_name = serializers.CharField(max_length = 100, required=True)
    age = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.IntegerField(required=True)
    ip_address = serializers.IPAddressField(required=True)
    mac_address = serializers.CharField(required=True)
    company = serializers.CharField(max_length = 100, required=True)
    role = serializers.CharField(max_length = 50, required=True)
    