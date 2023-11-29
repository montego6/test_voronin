from rest_framework import serializers
from users.models import CustomUser
from users.tasks import send_welcome_letter


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        username = user.username
        email = user.email
        send_welcome_letter.delay(email, username)
        return user
