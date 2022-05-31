from django.contrib.auth.models import Group
from django_rest_api.core.models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=30, required=True)
    password = serializers.CharField(max_length=30, min_length=8, required=True)
    first_name = serializers.CharField(allow_blank=True, max_length=30, required=False)
    last_name = serializers.CharField(allow_blank=True, max_length=30, required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
