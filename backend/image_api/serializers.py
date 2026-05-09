from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile


class CurrentUserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "last_login"]
        read_only_fields = ["username", "email", "last_login"]


class CurrentUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["theme", "font_size"]
