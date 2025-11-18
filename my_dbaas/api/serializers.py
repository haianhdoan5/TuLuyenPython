from django.contrib.auth.models import User

# model có sẵn trong django
from rest_framework import serializers


class User(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, user_info):
        user = User.objects.create_user(
            username=user_info["username"],
            email=user_info["email"],
            password=user_info["password"],
        )
        return user
